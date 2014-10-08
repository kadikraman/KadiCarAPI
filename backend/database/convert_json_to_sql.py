'''
This will read in data from data.json and convert it into a dict
Then will create or rewrite populate_db.py with the insert statements
to insert all the data that was in the JSON file to the expenses table
'''

import json
import time

json_data = open('data.json')

# load the json data into a dictionary
data = json.load(json_data)

# the string which will be written into file
sql = ''

for expense in data:
    sql += 'con.execute("""INSERT INTO expenses\n'

    # expense_type always in dict
    sql += '\t' + '(expense_type, \n \t'

    # amount always in dict
    sql += 'amount, \n \t'

    # mileage is nullable
    if('mileage' in expense):
        sql += 'mileage, \n \t'

    # litres is mullable
    if('litres' in expense):
        sql += 'litres, \n \t'

    # comment is nullable
    if('comment' in expense):
        sql += 'comment, \n \t'

    # expense_date always in dict
    sql += 'expense_date) \n'

    sql += 'VALUES  \n'

    # expense_type always in dict
    sql += '\t' + '(\'' + expense['expense_type'] + '\', \n'

    # amount always in dict
    sql += '\t' + str(expense['cost']) + ', \n'

    # mileage is nullable
    if('mileage' in expense):
        sql += '\t' + str(expense['mileage']) + ', \n'

    # litres is nullable
    if('litres' in expense):
        sql += '\t' + str(expense['litres']) + ', \n'

    # comment is nullable
    if('comment' in expense):
        sql += '\t' + '\'' + str(expense['comment']) + '\'' + ', \n'

    # expense_date always in dict
    sql += '\t' + '\'' + expense['expense_date'] + '\')""") \n \n'


# open the file (this creates the file if it didn't already exist)
file = open('populate_db.py', 'w')
file.close()

# open the file (this erases the contents if there was anything there previously)
file = open('populate_db.py', 'r+')
file.truncate()

# autogenerated file warning
file.write('\'\'\' \n' + 'This is an autogenerated file. \n')
file.write('This file was generated by convert_json_to_sql.py at ' + str(time.strftime("%c")) + '. \n')
file.write('Any edits will be overwritten. \n' + '\'\'\' \n \n')

# beginning statements
file.write('import sqlite3 \n \n')
file.write('con = sqlite3.connect(\'expenses.db\') \n \n')

# write all the sql we constructed above
file.write(sql)

#end statement
file.write('con.commit()')

# close the file
file.close()
