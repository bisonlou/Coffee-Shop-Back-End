from api import app
from flask import jsonify


@app.route('/api/v1/drinks')
def list_drinks():
    return jsonify({
        'success': True,
        'drinks': [
            {
                'id': 1,
                'title': 'matcha shake',
                'recipe': [
                    {
                        'name': 'milk',
                        'color': 'grey',
                        'parts': 1
                    },
                    {
                        'name': 'matcha',
                        'color': 'green',
                        'parts': 3
                    },
                ]
            },
            {
                'id': 2,
                'title': 'flatwhite',
                'recipe': [

                    {
                        'name': 'milk',
                        'color': 'grey',
                        'parts': 3
                    },
                    {
                        'name': 'coffee',
                        'color': 'brown',
                        'parts': 1
                    },
                ]
            },
            {
                'id': 3,
                'title': 'cap',
                'recipe': [
                    {
                        'name': 'foam',
                        'color': 'white',
                        'parts': 1
                    },
                    {
                        'name': 'milk',
                        'color': 'grey',
                        'parts': 2
                    },
                    {
                        'name': 'coffee',
                        'color': 'brown',
                        'parts': 1
                    },
                ]
            }
        ]
    }), 200


'''

@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
