import unittest
from main import app


class TestFlaskRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        response = self.app.get('/add?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'15')

    def test_sub(self):
        response = self.app.get('/sub?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'5')

    def test_mul(self):
        response = self.app.get('/mul?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'50')

    def test_div(self):
        response = self.app.get('/div?a=10&b=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'2.0')

    def test_add_error(self):
        response = self.app.get('/add?a=ten&b=five')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")

    def test_sub_error(self):
        response = self.app.get('/sub?a=ten&b=five')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")

    def test_mul_error(self):
        response = self.app.get('/mul?a=ten&b=five')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")

    def test_div_error(self):
        response = self.app.get('/div?a=ten&b=five')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Error: Please provide valid integer values for the 'a' and 'b' parameters.")


if __name__ == '__main__':
    unittest.main()
