import unittest
from api import app


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def test_get_drinks(self):
        response = self.client().get('/drinks').get_json()
        print(response)
        self.assertTrue(response['success'])


if __name__ == '__main__':
    unittest.main()
