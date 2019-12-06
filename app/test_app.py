from base64 import b64encode
from flask_api import status

import app
import app.config
import pytest


@pytest.fixture
def client():
    """ Factory function to provide client parameter to tests. """
    client = app.app.test_client()
    return client


@pytest.fixture
def admin_credentials():
    """ Factory function to provide admin_credentials to tests. """
    return app.config.ADMIN_CREDENTIALS


def make_credential_headers(credentials=app.config.ADMIN_CREDENTIALS):
    encoded_credentials = b64encode(
        '{c[0]}:{c[1]}'.format(c=credentials).encode('utf-8')
    ).decode('utf-8')
    payload = {'Authorization': 'Basic ' + encoded_credentials}
    return payload


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


def test_admin_login_failure(client, admin_credentials):
    """ Test logging in with incorrect admin credentials. """
    usr_name, password = admin_credentials

    # Test with incorrect usr_name
    credential_invalid_usr_name = (usr_name + '1', password)
    headers = dict(make_credential_headers(credential_invalid_usr_name))
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Test with incorrect password
    credential_invalid_password = (usr_name, password + '1')
    headers = dict(make_credential_headers(credential_invalid_password))
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Test with incorrect usr_name and password
    credential_invalid = (usr_name + '1', password + '1')
    headers = dict(make_credential_headers(credential_invalid))
    response = client.get('admin', headers=headers, follow_redirects=True)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_admin_login_success(client, admin_credentials):
    """ Test logging in with correct admin credentials. """
    headers = dict(make_credential_headers(admin_credentials))
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
