import pytest
import app
import app.config


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

    # Don't know how to respond to a WWW-Authenticate, will work on
    # Next, try logging in with the correct credentials
    """
    response = login(client, app.config.ADMIN_CREDENTIALS[0], app.config.ADMIN_CREDENTIALS[1])
    print(response)
    """


def test_retrieve_map_points(client):
    """ Test retrieval of the list of points on the map.
        Currently the points are random so this test is subject to change. """
    X_INTERVAL_LOW, X_INTERVAL_HIGH = 48.8434100, 48.8634100
    Y_INTERVAL_LOW, Y_INTERVAL_HIGH = 2.3388000, 2.3588000

    # Retrieve the points using a POST, and convert it from a Flask Response object to a dict
    points = client.post('/map/refresh', follow_redirects=True).get_json()
    # Check that each point is within range (arbitrary, subject to change once we have real data)
    for point in points['points']:
        """ pytest.approx() doesn't support 'approx() <= value <= approx()', excuse the hack to check for equality """
        # X-coordinate check
        assert X_INTERVAL_LOW < point[0] or abs(X_INTERVAL_LOW - point[0]) == pytest.approx(0.0) \
            and X_INTERVAL_HIGH > point[0] or abs(X_INTERVAL_HIGH - point[0]) == pytest.approx(0.0)

        # Y-coordinate check
        assert Y_INTERVAL_LOW < point[1] or abs(Y_INTERVAL_LOW - point[1]) == pytest.approx(0.0) \
            and Y_INTERVAL_HIGH > point[1] or abs(Y_INTERVAL_HIGH - point[1]) == pytest.approx(0.0)


'''
def test_app(app):
    """ Master function to call all tests, placeholder until I properly configure pytest... """
    global client = app.test_client()

    test_http_ok(client)
    test_http_not_found(client)
    test_admin_login_success(client)
    test_retrieve_map_points(client)
'''
