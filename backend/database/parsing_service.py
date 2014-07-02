__author__ = 'krak'

"""
The middleman between the server and data service.
Handles requests from the server and returns db queries in the desired format.
"""

import data_service


def get_expense_by_id(expense_id, requested_return_type):
    """
    Queries the db for the desired expense by id and returns
    the expense in the desired format
    :param expense_id: the id of the expense
    :param requested_return_type: format in which the result should be given
    :return: the expense in the desired format (e.g dict) (default: named tuple)
    """
    named_tuple = data_service.get_expense_by_id(expense_id)

    if requested_return_type == 'dict':
        return named_tuple_to_dict(named_tuple)

    return named_tuple


def get_expense_by_type(expense_type, requested_return_type):
    """
    Queries the database for the required expense type and returns
    the list of matching expenses in the desired format.

    :param expense_type: type of expense requested (e.g. petrol, maintenance)
    :param requested_return_type: format in which the result should be given
    :return: a list of expenses in the desired format (e.g. dict) (default: named tuple)
    """
    named_tuple_list = data_service.get_expenses_by_type(expense_type)

    return named_tuple_list_to_dict(named_tuple_list)


def named_tuple_list_to_dict(named_tuple_list):
    """
    Converts a named tuple list to a dict

    :param named_tuple_list: a list of expenses each in the form of a named tuple
    :return: the list of expenses as a dict
    """
    expense_list = []

    for tuple in named_tuple_list:
        expense_list.append(named_tuple_to_dict(tuple))

    return expense_list


def named_tuple_to_dict(named_tuple):
    """
    Converts a single named tuple to a dict

    :param named_tuple: the named tuple
    :return: dict
    """
    dictionary = {}
    for field in named_tuple._fields:
        # Create a dictionary key for each field in tuple and
        # enter the corresponding value by asking the
        # the object if it has an attribute/property with 
        # name of the field, and if so, return the value.
        dictionary[field] = getattr(named_tuple, field)

    return dictionary