import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from google.cloud import datastore
from google.auth.transport import requests
import google.oauth2.id_token

datastore_client = datastore.Client()

firebase_request_adapter = requests.Request()

app = Flask(__name__)
app.secret_key = 'fsdfsdfowe2323r'


@app.route('/', methods=['GET', 'POST'])
def root():
    id_token = request.cookies.get("token")
    claims, error_message = auth()
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
        items = list(items)

    if request.method == 'GET':
        return render_template('index.html', user=claims, error_message=error_message, items=items)
    elif request.method == 'POST':
        name = request.form['name']
        qty = request.form['qty']
        store_item(claims['email'], datetime.datetime.now(), name, qty)
        flash('%s successfully added' % name, 'added')
        return redirect(url_for('root'))


@app.route('/delete/<int:item>/', methods=['GET', 'POST'])
def delete(item):
    """
    Deletes a single Item from the Database
    :param item:
    :return:
    """
    claims, error_message = auth()

    if claims:
        delete_item('User', claims['email'], 'visit', item, 'Item')
    return redirect(url_for('root'))


@app.route('/delete_all/', methods=['GET', 'POST'])
def delete_all():
    """
    Deletes all items from the database
    :return:
    """
    claims, error_message = auth()
    if claims:
        items = fetch_times(claims['email'])
        for item in items:
            delete_item('User', claims['email'], 'visit', item.id, item['item_name'])
    return redirect(url_for('root'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect(url_for('root'))


def fetch_times(email):
    """
    Fetch all items from the database using User email as filter and order the items by time
    :param email:
    :return:
    """
    ancestor = datastore_client.key('User', email)
    query = datastore_client.query(kind='visit', ancestor=ancestor)
    query.order = ['-timestamp']

    items = query.fetch()

    return items


def store_item(email, dt, name, qty):
    """
    Save Shopping items to the data base
    :param email:
    :param dt:
    :param name:
    :param qty:
    :return:
    """
    entity = datastore.Entity(key=datastore_client.key('User', email, 'visit'))
    entity.update({
        'timestamp': dt,
        'item_name': name,
        'item_qty': qty

    })

    datastore_client.put(entity)


def delete_item(user, email, entity, item_id, element):
    """
    Helper Function to delete specific item from the data store
    :param user:
    :param email:
    :param entity:
    :param item_id:
    :param element:
    :return:
    """
    key = datastore_client.key(user, email, entity, item_id)
    datastore_client.delete(key)
    flash('%s successfully deleted' % element, 'deleted')


def auth():
    """
    Retrieve, verify, and decrypt the firebase token
    :return:
    """
    id_token = request.cookies.get("token")
    error_message = None
    claims = None

    if id_token:
        try:
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)

    return claims, error_message


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
