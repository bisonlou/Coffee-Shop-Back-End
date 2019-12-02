
# COFFEE SHOP API Backend

[![Build Status](https://travis-ci.org/bisonlou/Coffee-Shop-Back-End.svg?branch=develop)](https://travis-ci.org/bisonlou/Coffee-Shop-Back-End)
[![Maintainability](https://api.codeclimate.com/v1/badges/bad403a1ad5903bbab37/maintainability)](https://codeclimate.com/github/bisonlou/Coffee_Shop_API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/bisonlou/Coffee-Shop-Back-End/badge.svg?branch=develop)](https://coveralls.io/github/bisonlou/Coffee-Shop-Back-End?branch=develop)

Welcome to the Coffee Shop backend API. This backend serves the Coffee Shop frontend with drink menus.
Find the live backend hosted [here](https://coffee-shop-backend.herokuapp.com/api/v1)

This backend was built following [PEP8](https://www.python.org/dev/peps/pep-0008/) standards.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

The sqlite databases are provided in the database folder under the api

## Running the server

From within the `root` directory first ensure you are working using your created virtual environment.

To run the server, create a .env file.

```bash
    touch .env
```

Inside the .env file, export your database URIs

```bash
export AUTH0_DOMAIN='your Oauth domain name'
export ALGORITHMS=['your Oauth algorithm']
export API_AUDIENCE='your API audience'
```

Then excecute:

```bash
py app.py
```

```bash

Endpoints
GET 'api/v1/drinks'
GET 'api/v1/drinks/<int:drink_id>'
POST 'api/v1/drinks'
PATCH '/api/v1/drinks/<int:drink_id>'
DELETE '/api/v1/drinks/<int:drink_id>'
```

```bash

curl http://127.0.0.1:5000/api/v1/drinks

- Fetches a list of drinks
- Returns:
{
  "drinks": [
    {
      "id": 1,
      "title": "capuchino"
    },
    {
      "id": 2,
      "title": "late"
    },
    {
      "id": 3,
      "title": "chilotte"
    },
    {
      "id": 4,
      "title": "spiced latte"
    },
  ]
  "success": true
}

```

```bash

curl http://127.0.0.1:5000/api/v1/drinks/1 -H "Authorization: Bearer {{token}}"

- Fetches drink details
- Returns:
{
  "drinks": {
    "id": 1,
    "recipe": [
      {
        "color": "yellow",
        "name": "milk",
        "parts": "1"
      },
      {
        "color": "brown",
        "name": "water",
        "parts": "2"
      }
    ],
    "title": "capuchino"
  },
  "success": true
}
  ```

```bash

curl -X DELETE http://127.0.0.1:5000/api/v1/drinks/20 -H "Authorization: Bearer {{token}}"

- Deletes a drink
- Returns:
{
    "delete": 20,
    "success": true
}
```

```bash

curl  http://127.0.0.1:5000/api/v1/drinks -X POST
-H "Content-Type: application/json" 
-H "Authorization: Bearer {{token}}" 
-d '{"title": "Capuchino7","recipes": [{"name":      "milk", "color":"cream", "parts": 3},              {"name":"coffee", color":"brown", "parts": 1}]}'

- Posts a drink
- Returns:
{
    "drink": {
        "id": 26,
        "recipe": [
            {
                "color": "cream",
                "name": "milk",
                "parts": "3"
            },
            {
                "color": "brown",
                "name": "coffee",
                "parts": "1"
            }
        ],
        "title": "Capuchino7"
    },
    "success": true
}
```

```bash

curl  http://127.0.0.1:5000/api/v1/drinks/26
-X PATCH
-H "Content-Type: application/json"
-H "Authorization: Bearer {{token}}"
-d '{"title": "Capuchino7", "recipes": [{"name": "milk", "color":"cream", "parts": 3},
{"name":"coffee", "color":"brown", "parts": 1}]
}'

- Updates a drink
- Returns:
{
    "drink": {
        "id": 26,
        "recipe": [
            {
                "color": "cream",
                "drink": 26,
                "id": 35,
                "name": "milk",
                "parts": "3"
            },
            {
                "color": "brown",
                "drink": 26,
                "id": 36,
                "name": "coffee",
                "parts": "1"
            }
        ],
        "title": "Capuchino7"
    },
    "success": true
}
```

```bash

## Error Handling

Errors are returned as JSON objects in the following format:

```bash
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

The API will return five error types when requests fail:

400: Bad Request

```bash
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

404: Resource Not Found

```bash
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

405: Method Not Allowed

```bash
{
    "success": False,
    "error": 405,
    "message": "method not allowed"
}
```

422: Not Processable

```bash
{
    "success": False,
    "error": 422,
    "message": "unable to process request"
}
```

500: Internal Server Error

```bash
{
    "success": False,
    "error": 500,
    "message": "internal server error"
}
```

## Testing

To run the tests, run

```bash
pytest
```
