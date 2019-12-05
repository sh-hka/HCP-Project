from base64 import b64encode
from flask_api import status

import app
import app.config
import pytest


def login(client, username, password, url='admin'):
    """ Helper function to assist with logging in with a set of credentials. """
    return client.post(
        url, data=dict(username=username, password=password), follow_redirects=True
    )


@pytest.fixture
def client():
    """ Set-up function to be run before each test. """
    client = app.app.test_client()
    return client


def test_http_ok_landing(client):
    """ Basic testing to ensure landing page responds with HTTP OK (200). """
    response = client.get('/', follow_redirects=True)
    assert response.status_code == status.HTTP_200_OK


def test_http_ok_index(client):
    """ Basic testing to ensure index page responds with HTTP OK (200)"""
    response = client.get('index', follow_redirects=True)
    assert response.status_code == status.HTTP_200_OK


def test_http_ok_contact(client):
    """ Basic testing to ensure contact page responds with HTTP OK (200)"""
    response = client.get('contact', follow_redirects=True)
    assert response.status_code == status.HTTP_200_OK


def test_http_ok_search(client):
    """ Basic testing to ensure contact page responds with HTTP OK (200)"""
    response = client.get('search', follow_redirects=True)
    assert response.status_code == status.HTTP_200_OK


def test_http_not_found1(client):
    """ Test an invalid URL(asdf) and make sure we get HTTP Page Not Found (404). """
    response = client.get('asdf', follow_redirects=True)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_http_not_found2(client):
    """ Test an invalid URL(map) and make sure we get HTTP Page Not Found (404). """
    response = client.get('map', follow_redirects=True)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_admin_login_failure(client):
    """ Test logging in with incorrect admin credentials. """
    cred = b64encode('{cred[0]}1:{cred[1]}'.format(cred=app.config.ADMIN_CREDENTIALS).encode('utf-8')).decode('utf-8')
    headers = {'Authorization': 'Basic ' + cred}
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    cred = b64encode('{cred[0]}:{cred[1]}1'.format(cred=app.config.ADMIN_CREDENTIALS).encode('utf-8')).decode('utf-8')
    headers = {'Authorization': 'Basic ' + cred}
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    cred = b64encode('{cred[0]}1:{cred[1]}1'.format(cred=app.config.ADMIN_CREDENTIALS).encode('utf-8')).decode('utf-8')
    headers = {'Authorization': 'Basic ' + cred}
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_admin_login_success(client):
    """ Test logging in with correct admin credentials. """
    cred = b64encode('{cred[0]}:{cred[1]}'.format(cred=app.config.ADMIN_CREDENTIALS).encode('utf-8')).decode('utf-8')
    headers = {'Authorization': 'Basic ' + cred}
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_200_OK


if __name__ == '__main__':
    pytest.main(['-v', '-W ignore::DeprecationWarning'])

'''
def test_app(app):
    """ Master function to call all tests, placeholder until I properly configure pytest... """
    global client = app.test_client()

    test_http_ok(client)
    test_http_not_found(client)
    test_admin_login_success(client)
    test_retrieve_map_points(client)
'''
