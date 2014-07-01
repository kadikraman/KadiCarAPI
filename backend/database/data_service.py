"""
Handles the interaction with an SQLite database
"""

import sqlite3
from collections import namedtuple


def namedtuple_factory(cursor, row):
    """
    Usage:
    con.row_factory = namedtuple_factory
    """
    fields = [col[0] for col in cursor.description]
    Row = namedtuple("Row", fields)
    return Row(*row)


def get_all_expenses():
    """
    Returns all expenses in the db
    """
    conn = sqlite3.connect("database/expenses.db")
    connection_cursor = conn.cursor()
    connection_cursor.execute("SELECT type, date, amount FROM expenses")
    result = connection_cursor.fetchall()
    connection_cursor.close()
    conn.commit()
    conn.close()
    return result


def get_expenses_by_type(expense_type):
    """
    Returns all expenses of the given type
    """
    conn = sqlite3.connect("database/expenses.db")
    conn.row_factory = namedtuple_factory
    connection_cursor = conn.cursor()
    connection_cursor.execute("""SELECT * 
                                 FROM expenses 
                                 WHERE type = '{0}'""".format(expense_type))
    result = connection_cursor.fetchall()
    connection_cursor.close()
    conn.commit()
    conn.close()
    return result


def get_expense_by_id(expense_id):
    """
    Returns the expenses of the given id
    """
    conn = sqlite3.connect("database/expenses.db")
    conn.row_factory = namedtuple_factory
    connection_cursor = conn.cursor()
    connection_cursor.execute("""SELECT * 
                                 FROM expenses 
                                 WHERE id = {0}""".format(expense_id))
    result = connection_cursor.fetchone()
    connection_cursor.close()
    conn.commit()
    conn.close()
    return result
