from nose.tools import assert_equal
from main import app  # replace 'your_flask_app' with the name of the file your Flask app is in

app.testing = True
client = app.test_client()


def test_add():
    response = client.get('/add?a=10&b=5')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b'15')


def test_sub():
    response = client.get('/sub?a=10&b=5')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b'5')


def test_mul():
    response = client.get('/mul?a=10&b=5')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b'50')


def test_div():
    response = client.get('/div?a=10&b=5')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b'2.0')


def test_add_error():
    response = client.get('/add?a=ten&b=five')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")


def test_sub_error():
    response = client.get('/sub?a=ten&b=five')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")


def test_mul_error():
    response = client.get('/mul?a=ten&b=five')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")


def test_div_error():
    response = client.get('/div?a=ten&b=five')
    assert_equal(response.status_code, 200)
    assert_equal(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")
