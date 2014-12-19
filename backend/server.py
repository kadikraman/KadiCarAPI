"""
Handles requests from the client
"""
import json
from database import parsing_service
from bottle import route, run, get, template, debug, static_file

@route("/")
@route("/home")
def hello_kadicar():
    return static_file('index.html', root='../frontend')

# Static files such as images or CSS files are not served automatically
# Added a route and a callback to control which files get served and where to find them
# currently serving everything linked to from /frontend/static (js, css etc)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='../frontend/static')

@get("/data/all_expenses")
def all_expenses():
    """
    It does stuff
    """
    return json.dumps(parsing_service.get_all_expenses('dict'))

@get("/data/get_expense_by_id/:expense_id")
def get_one_expense(expense_id):
    """
    Get an expense by id
    """
    expense = parsing_service.get_expense_by_id(expense_id, 'dict')

    #expense = {"Type": "Vroom money",
    #           "Monies": "Some"}

    return json.dumps(expense)

@get("/data/dashboard")
def get_dashboard():
    """
    Testing templates
    """
    result = parsing_service.get_all_expenses('key-value')
    output = template('make_table', rows=result)
    return output

@get("/get_expenses_by_type/:expense_type")
def get_expenses_by_type(expense_type):
    """
    Get the expense of a particular type
    """
    expense = parsing_service.get_expenses_by_type(expense_type, 'dict')
    return json.dumps(expense)

run(host='localhost', port=8000, debug=True)
