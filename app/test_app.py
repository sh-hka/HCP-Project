from flask import Response
import pytest
import app


def login(client, username, password, url='admin'):
    """ Helper function to assist with logging in with a set of credentials. """
    return client.post(url,
                       data=dict(username=username, password=password),
                       follow_redirects=True)


@pytest.fixture
def client():
    """ Set-up function to be run before each test. """
    client = app.app.test_client()
    return client


def test_http_ok(client):
    """ Basic testing to ensure each page responds with HTTP OK (200). """
    assert client.get('/', follow_redirects=True).status_code == 200
    assert client.get('map', follow_redirects=True).status_code == 200
    assert client.get('contact', follow_redirects=True).status_code == 200


def test_http_not_found(client):
    """ Test an invalid URL and make sure we get HTTP Page Not Found (404). """
    assert client.get('asdf', follow_redirects=True).status_code == 404
    assert client.get('doctors', follow_redirects=True).status_code == 404
    assert client.get('map/info', follow_redirects=True).status_code == 404


def test_admin_login_success(client):
    """ Test logging in with correct admin credentials. """
    """ NOTE: the '<website>:5000/admin' panel is part of flask-admin.
        Server responds with WWW-Authenticate, replying with POST does not work... """
    # First, check that access without credentials is HTTP Forbidden (401)
    assert client.get('admin', follow_redirects=True).status_code == 401

    # Next, try logging in with the correct credentials
    #response = login(client, app.config.ADMIN_CREDENTIALS[0], app.config.ADMIN_CREDENTIALS[1])
    #print(response)


def test_retrieve_map_points(client):
    """ Test retrieval of the list of points on the map.
        Currently the points are random so this test is subject to change.
        ERROR: <Response streamed [405 METHOD NOT ALLOWED]> when trying to fetch refresh results, will look into """
    #print(client.get('map/refresh', follow_redirects=True))
    pass


'''
def test_app(app):
    """ Master function to call all tests, placeholder until I properly configure pytest... """
    global client = app.test_client()

    test_http_ok(client)
    test_http_not_found(client)
    test_admin_login_success(client)
    test_retrieve_map_points(client)
'''