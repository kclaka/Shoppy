import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from google.cloud import datastore
from google.auth.transport import requests
import google.oauth2.id_token

datastore_client = datastore.Client()

firebase_request_adapter = requests.Request()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    items = None

    if id_token:
        try:
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)

    if claims:
        items = fetch_times(claims['email'])

    if request.method == 'GET':
        return render_template('index.html', user=claims, error_message=error_message, items=items)
    elif request.method == 'POST':
        name = request.form['name']
        qty = request.form['qty']
        store_item(claims['email'], datetime.datetime.now(), name, qty)
        return redirect(url_for('root'))


def store_item(email, dt, name, qty):
    entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
    entity.update({
        'timestamp': dt,
        'item_name': name,
        'item_qty': qty

    })

    datastore_client.put(entity)


def fetch_times(email):
    ancestor = datastore_client.key('User', email)
    query = datastore_client.query(kind='visit', ancestor=ancestor)
    query.order = ['-timestamp']

    items = query.fetch()

    return items


def delete_item(user, email, entity, item_id, element):
    key = datastore_client.key(user, email, entity, item_id)
    datastore_client.delete(key)
    flash('%s successfully deleted' % element, 'deleted')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
