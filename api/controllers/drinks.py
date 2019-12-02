import sys
from api import app
from api.database import db
from api.models.drink import Drink
from api.auth import requires_auth
from api.models.recipe import Recipe
from flask import jsonify, abort, request


"""
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where
    drinks is the list of drinks
        or appropriate status code indicating reason for failure
"""


@app.route("/api/v1/drinks")
def list_drinks():
    drink_list = Drink.query.all()

    drinks = []
    for drink in drink_list:
        recipes = Recipe.query.filter(Recipe.drink_id == drink.id).all()

        drinks.append(
            {
                "id": drink.id,
                "title": drink.title,
                "recipe": [
                    {
                        "name": recipe.name,
                        "color": recipe.color,
                        "parts": recipe.parts,
                    }
                    for recipe in recipes
                ],
            }
        )

    return jsonify({"success": True, "drinks": drinks}), 200


"""
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where
    drinks is the list of drinks
        or appropriate status code indicating reason for failure
"""


"""
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where
    drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
"""


@app.route("/api/v1/drinks", methods=["POST"])
@requires_auth('post:drinks')
def add_drinks(payload):
    if not request.json:
        abort(400)

    title = request.json.get("title", None)
    recipes = request.json.get("recipes", None)

    if title and recipes:
        if Drink.query.filter(Drink.title == title).count() > 0:
            return jsonify(
                {
                    "success": False,
                    'message': 'drink already exists'
                }
            ), 200

        drink = Drink(title=title)

        # add recipes to drink
        for recipe in recipes:
            recipe = Recipe(
                name=recipe["name"],
                color=recipe["color"],
                parts=recipe["parts"],
            )

            drink.recipe.append(recipe)

        error = False

        try:
            drink.insert()
        except Exception:
            error = True
            print(sys.exc_info())
        finally:
            db.session.close()

        if not error:
            return jsonify({"success": True}), 200

        abort(422)


"""
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where
    drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
"""


"""
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where
    id is the id of the deleted record
        or appropriate status code indicating reason for failure
"""
