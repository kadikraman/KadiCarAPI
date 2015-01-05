import os
from subprocess import call

# Delete the old database
try:
    os.remove('expenses.sqlite')
except OSError:
    pass

# Build a new database
call(['python', 'create_db.py'])

# update the insert statements
call(['python', 'convert_json_to_sql.py'])

# Populate the the database with default data
call(['python', 'populate_db.py'])

print("Rebuild successful")