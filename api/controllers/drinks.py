import sys
from api import app
from api.database import db
from api.models.drink import Drink
from api.auth import requires_auth
from api.models.recipe import Recipe
from flask import jsonify, abort, request
from api.validators import validate_drink


@app.route("/api/v1/drinks")
def list_drinks():
    drinks = Drink.query.all()

    return jsonify({"success": True, "drinks": list(
                    map(lambda drink: drink.short(), drinks))
                    }), 200


@app.route('/api/v1/drinks-detail/<int:drink_id>')
@requires_auth('get:drinks-detail')
def retrieve_drink(payload, drink_id):
    drink = Drink.query.get_or_404(drink_id, "drink not found")

    return jsonify({
        "success": True,
        "drinks": {
            "id": drink.id,
            "title": drink.title,
            "recipe": [
                {
                    "name": recipe.name,
                    "color": recipe.color,
                    "parts": recipe.parts,
                }
                for recipe in drink
            ],
        }}), 200


@app.route("/api/v1/drinks", methods=["POST"])
@requires_auth('post:drinks')
def add_drinks(payload):

    validate_drink(request)

    title = request.json.get("title", None)
    recipes = request.json.get("recipes", None)

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
        drink_id = drink.insert()
        print(drink_id)
    except Exception:
        error = True
        print(sys.exc_info())
        abort(422)
    finally:
        db.session.close()

    if not error:
        drink = Drink.query.get_or_404(drink_id)

        return jsonify({
            "success": True,
            "drink": {
                "id": drink.id,
                "title": drink.title,
                "recipe": [
                    {
                        "name": recipe.name,
                        "color": recipe.color,
                        "parts": recipe.parts,
                    }
                    for recipe in drink.recipe
                ],
            }
        }), 200


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
@app.route('/api/v1/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(payload, drink_id):
    validate_drink(request)

    drink = Drink.query.get_or_404(drink_id)

    title = request.json.get("title", None)
    recipes = request.json.get("recipes", None)

    error = False
    try:
        for recipe in drink.recipe:
            recipe.delete()

        drink.title = title

        for recipe in recipes:
            recipe = Recipe(
                name=recipe["name"],
                color=recipe["color"],
                parts=recipe["parts"],
            )

            drink.recipe.append(recipe)

        drink.update()
    except Exception:
        error = True
        print(sys.exc_info())
        abort(422)

    if not error:
        return jsonify({
            'success': True,
            'drink': {
                'id': drink.id,
                'title': drink.title,
                'recipe': [recipe.short() for recipe in drink.recipe]
            }
        })


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

@app.route('/api/v1/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    drink = Drink.query.get_or_404(drink_id, "drink not found")

    error = False

    try:
        drink.delete()
    except Exception:
        print(sys.exc_info())
        error = True
        abort(422)

    if not error:
        return jsonify({
            'success': True,
            'delete': drink.id
        })
