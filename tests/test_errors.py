from api import app
import unittest


class ErrorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def test_404(self):
        response = self.client().get("/api/v1/drink")
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data["success"])

    def test_405(self):
        response = self.client().put("/api/v1/drinks")
        data = response.get_json()

        self.assertEqual(response.status_code, 405)
        self.assertFalse(data["success"])


if __name__ == "__main__":
    unittest.main()
