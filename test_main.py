import unittest
import requests


class CalcTests(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:5000'

    def test_add(self):
        response = requests.get('http://localhost:5000/add?a=1&b=2')
        self.assertEqual(response.text, '3')

    def test_sub(self):
        response = requests.get('http://localhost:5000/sub?a=1&b=2')
        self.assertEqual(response.text, '-1')

    def test_mul(self):
        response = requests.get('http://localhost:5000/mul?a=1&b=2')
        self.assertEqual(response.text, '2')

    def test_div(self):
        response = requests.get('http://localhost:5000/div?a=1&b=2')
        self.assertEqual(response.text, '0.5')


if __name__ == '__main__':
    unittest.main()
