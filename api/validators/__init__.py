from flask import abort


def validate_drink(request):
    if not request.json:
        abort(400, "json data expected")

    title = request.json.get("title", None)
    recipes = request.json.get("recipes", None)

    if not title:
        abort(400, "drink title expected")

    if title == "":
        abort(400, "drink title cannot be empty")

    if type(title) is not str:
        abort(400, "drink title must be of type string")

    if type(recipes) is not list:
        abort(400, "recipes must be of type list")

    if not recipes:
        abort(400, "recipes expected")

    if len(recipes) == 0:
        abort(400, "recipes cannot be empty")

    for recipe in recipes:
        if 'name' not in recipe:
            abort(400, "recipe name expected")

        if recipe['name'] == "":
            abort(400, "recipe name cannot be empty")

        if 'color' not in recipe:
            abort(400, "recipe color expected")

        if recipe['color'] == "":
            abort(400, "recipe color cannot be empty")

        if 'parts' not in recipe:
            abort(400, "recipe parts expected")

        if type(recipe['name']) is not str:
            abort(400, "recipe name must be of type string")

        if type(recipe['color']) is not str:
            abort(400, "recipe color must be of type string")

        if type(recipe['parts']) is not int:
            abort(400, "recipe parts must be of type int")
