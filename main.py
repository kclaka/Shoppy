import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from google.cloud import datastore
from google.auth.transport import requests
import google.oauth2.id_token

datastore_client = datastore.Client()

firebase_request_adapter = requests.Request()

app = Flask(__name__)


@app.route('/')
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
        return render_template('index.html', user = claims, error_message=error_message, items=items)
    elif request.method == 'POST':
        item_name = request.form['shop-item']
        item_no = request.form['item-no']
        store_item(claims['email'], datetime.datetime.now(), item_name)
        return redirect(url_for('root'))


@app.route('/test')
def test():
    store_item(datetime.datetime.now())

    times = fetch_times(10)
    return render_template('test.html', times=times)


def store_item(email, dt, item_name, item_no):
    entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
    entity.update({
        'timestamp': dt,
        'item_name': item_name,
        'item_no': item_no

    })

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
