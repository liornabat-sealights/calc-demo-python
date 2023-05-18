import pytest
from main import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_add(client):
    response = client.get('/add?a=10&b=5')
    assert response.status_code == 200
    assert response.data == b'15'


def test_sub(client):
    response = client.get('/sub?a=10&b=5')
    assert response.status_code == 200
    assert response.data == b'5'


def test_mul(client):
    response = client.get('/mul?a=10&b=5')
    assert response.status_code == 200
    assert response.data == b'50'


def test_div(client):
    response = client.get('/div?a=10&b=5')
    assert response.status_code == 200
    assert response.data == b'2.0'


def test_add_error(client):
    response = client.get('/add?a=ten&b=five')
    assert response.status_code == 200
    assert response.data == b"Error: Please provide valid integer values for the 'a' and 'b' parameters."


def test_sub_error(client):
    response = client.get('/sub?a=ten&b=five')
    assert response.status_code == 200
    assert response.data == b"Error: Please provide valid integer values for the 'a' and 'b' parameters."


def test_mul_error(client):
    response = client.get('/mul?a=ten&b=five')
    assert response.status_code == 200
    assert response.data == b"Error: Please provide valid integer values for the 'a' and 'b' parameters."


def test_div_error(client):
    response = client.get('/div?a=ten&b=five')
    assert response.status_code == 200
    assert response.data == b"Error: Please provide valid integer values for the 'a' and 'b' parameters."
