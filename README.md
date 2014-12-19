KadiCarAPI
==========

API for the car expenses data

Slowly but surely transitioning to a full stack thing.
Currently Python backend with sqlite3, bottle server, javascript angular frontend and a d3 wrapper (dimple.js) for visualisations.

# Creating the DB
Navigate to /backend/database and run "python rebuild_db.py" - this will create expenses.db based on the json data (data.json) in the same folder.

# Running the application
Navigate to /backend and run "python server.py" - this will start the server at localhost:8000

# Dependencies
There are some. I will make a thing to auto-install them eventually.