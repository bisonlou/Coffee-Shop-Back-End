import sys
from api import app
from api.models.drink import Drink
from api.auth import requires_auth
from api.models.recipe import Recipe
from flask import jsonify, abort, request
from api.validators import validate_drink


@app.route("/api/v1/drinks")
def list_drinks():
    """
    lists all drinks in the db
    """

    drinks = Drink.query.all()

    return (
        jsonify(
            {
                "success": True,
                "drinks": list(map(lambda drink: drink.short(), drinks)),
            }
        ),
        200,
    )


@app.route("/api/v1/drinks-detail")
@requires_auth("get:drinks-detail")
def retrieve_drink(payload):
    """
    returns the details of all drinks
    """
    
    formated_drinks = [drink.short() for drink in Drink.query.all()]

    for drink in formated_drinks:
        drink['recipe'] = [recipe.short() for recipe in Recipe.query.filter(
            Recipe.drink_id == drink['id']).all()]

    return (
        jsonify(
            {
                "success": True,
                "drinks": formated_drinks,
            }
        ),
        200,
    )


@app.route("/api/v1/drinks", methods=["POST"])
@requires_auth("post:drinks")
def add_drinks(payload):
    """
    posts a drink to the database
    """

    validate_drink(request)

    title = request.json.get("title", None)
    recipes = request.json.get("recipes", None)

    if Drink.query.filter(Drink.title == title).count() > 0:
        return (
            jsonify({"success": False, "message": "drink already exists"}),
            200,
        )

    drink = Drink(title=title)

    # add recipes to drink
    for recipe in recipes:
        recipe = Recipe(
            name=recipe["name"], color=recipe["color"], parts=recipe["parts"],
        )

        drink.recipe.append(recipe)

    error = False

    try:
        drink_id = drink.insert()

    except Exception:
        error = True
        print(sys.exc_info())
        abort(422)

    if not error:
        return (
            jsonify(
                {
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
                    },
                }
            ),
            200,
        )


@app.route("/api/v1/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth("patch:drinks")
def update_drinks(payload, drink_id):
    """
    updates a drink
    """

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
        return jsonify(
            {
                "success": True,
                "drinks": [
                    {
                        "id": drink.id,
                        "title": drink.title,
                        "recipe": [recipe.short() for recipe in drink.recipe],
                    },
                ]
            }
        )


@app.route("/api/v1/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth("delete:drinks")
def delete_drink(payload, drink_id):
    """
    deletes a drink
    """

    drink = Drink.query.get_or_404(drink_id, "drink not found")

    error = False

    try:
        drink.delete()
    except Exception:
        print(sys.exc_info())
        error = True
        abort(422)

    if not error:
        return jsonify({"success": True, "delete": drink.id})
