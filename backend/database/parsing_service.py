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

    dictionary["type"] = named_tuple.type
    dictionary["amount"] = named_tuple.amount
    dictionary["date"] = named_tuple.date
    dictionary["comment"] = named_tuple.comment
    dictionary["mileage"] = named_tuple.mileage
    dictionary["litres"] = named_tuple.litres

    return dictionary