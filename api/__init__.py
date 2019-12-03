from flask import Flask
from flask_cors import CORS
from api.database import setup_db

app = Flask(__name__)
setup_db(app)
<<<<<<< HEAD
CORS(app)
=======
CORS(app, resources={r"/api/v1/*": {"origins": "*"}},
     supports_credentials=True)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,PATCH,OPTIONS')
    return response
>>>>>>> b08142d9c7f88f56e84d900004118738b589fec9

import api.controllers.drinks
import api.controllers.errors
import api.models.recipe
import api.models.drink
