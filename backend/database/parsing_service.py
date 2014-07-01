__author__ = 'krak'

from database import data_service


def get_expense_by_id(expense_id, requested_return_type):
    """

    :param expense_id:
    :return:
    """
    named_tuple = data_service.get_expense_by_id(expense_id)

    if requested_return_type == 'dict':
        return named_tuple_to_dict(named_tuple)

    return named_tuple


def get_expense_by_type(expense_type, requested_return_type):
    named_tuple_list = data_service.get_expenses_by_type(expense_type)

    return named_tuple_list_to_dict(named_tuple_list)

def named_tuple_list_to_dict(named_tuple_list):
    list = []

    for tuple in named_tuple_list:
        list.append(named_tuple_to_dict(tuple))

    return list

def named_tuple_to_dict(named_tuple):
    """
    Converts a named tuple row into a dictionary
    :rtype : dictionary
    """
    dictionary = {}
    for field in named_tuple._fields:
        # Create a dictionary key for each field in tuple and
        # enter the corresponding value by asking the
        # the object if it has an attribute/property with 
        # name of the field, and if so, return the value.
        dictionary[field] = getattr(named_tuple, field)

    return dictionary