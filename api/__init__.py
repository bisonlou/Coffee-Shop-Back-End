from flask import Flask
from flask_cors import CORS
from api.database import setup_db

app = Flask(__name__)
setup_db(app)
CORS(app)

import api.controllers.drinks
import api.controllers.errors
import api.models.recipe
import api.models.drink
