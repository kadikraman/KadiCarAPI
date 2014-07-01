"""
Does spoopy stuff
"""
import json
from database import data_service, parsing_service
from bottle import route, run, get, template, debug

@route('/all_expenses')
def all_expenses():
    """
    It does stuff
    """
    return json.dumps(data_service.get_all_expenses())

@get("/get_expense_by_id/:expense_id")
def get_one_expense(expense_id):
    """
    Get an expense by id
    """
    expense = parsing_service.get_expense_by_id(expense_id, 'dict')

    #expense = {"Type": "Vroom money",
    #           "Monies": "Some"}

    return json.dumps(expense)

@get("/dashboard")
def get_dashboard():
    """
    Testing templates
    """
    result = data_service.get_all_expenses()
    output = template('make_table', rows=result)
    return output

@get("/get_expenses_by_type/:expense_type")
def get_expenses_by_type(expense_type):
    """
    Get the expense of a particular type
    """
    expense = parsing_service.get_expense_by_type(expense_type, 'dict')
    return json.dumps(expense)

debug(True)
run(reloader=True)
run()
