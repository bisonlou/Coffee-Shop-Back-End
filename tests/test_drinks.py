import json
import unittest
from api import app
from api.models.drink import Drink
from api.database import setup_db, db
from api.models.recipe import Recipe
from unittest.mock import patch


class DrinkTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        setup_db(self.app, database_filename="test_database.db")
        self.client = self.app.test_client

        sample_drink = Drink(title="test drink")
        sample_recipe = Recipe(name="milk", color="white", parts=1)
        sample_drink.recipe.append(sample_recipe)

        sample_drink.insert()

    def tearDown(self):
        db.drop_all()

    @patch('api.auth.requires_auth')
    def mock_requres_auth(normal_argument, mock_class):
        return 'mock payload'

    def test_add_drink(self):
        body = {
            "title": "capuchino",
            "recipes": [
                {"name": "milk", "color": "yellow", "parts": 1},
                {"name": "water", "color": "brown", "parts": 2},
            ],
        }

        response = self.client().post(
            "/api/v1/drinks",
            content_type="application/json",
            data=json.dumps(body),
        )

        data = response.get_json()

        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    def test_add_drinks_without_data(self):
        body = {}

        response = self.client().post(
            "/api/v1/drinks",
            content_type="application/json",
            data=json.dumps(body),
        )

        self.assertEqual(response.status_code, 401)

    def test_get_drinks(self):
        response = self.client().get("/api/v1/drinks")
        data = response.get_json()

        self.assertTrue(data["success"])
        self.assertEqual(len(data["drinks"]), 1)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
