from api import app
from flask import jsonify


@app.errorhandler(422)
def unprocessable(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 422,
                "message": "unprocessable",
                "description": error.description,
            }
        ),
        422,
    )


@app.errorhandler(400)
def bad_data(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 400,
                "message": "bad data",
                "description": error.description,
            }
        ),
        400,
    )


@app.errorhandler(404)
def not_found(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 404,
                "message": "resource not found",
                "description": error.description,
            }
        ),
        404,
    )


@app.errorhandler(405)
def method_not_allowed(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 405,
                "message": "method not allowed",
                "description": error.description,
            }
        ),
        405,
    )


@app.errorhandler(403)
def unauthorized(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 403,
                "message": "unauthorized",
                "description": error.description,
            }
        ),
        403,
    )


@app.errorhandler(401)
def not_authenticated(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 401,
                "message": "not authenticated",
                "description": error.description,
            }
        ),
        401,
    )


@app.errorhandler(500)
def internal_server_error(error):
    return (
        jsonify(
            {
                "success": False,
                "error": 500,
                "message": "internal server error",
                "description": error.description,
            }
        ),
        500,
    )
