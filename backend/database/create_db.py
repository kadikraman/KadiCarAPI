import sqlite3

con = sqlite3.connect('expenses.sqlite')  # creates the file if it doesn't exist yet

con.execute("""CREATE TABLE expenses(
    id INTEGER PRIMARY KEY,
    expense_type CHAR(20) NOT NULL,
    amount REAL NOT NULL,
    expense_date CHAR(10) NOT NULL,
    mileage INTEGER,
    litres INTEGER,
    comment CHAR(100)
)""")

con.commit()
