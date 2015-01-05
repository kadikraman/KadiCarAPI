KadiCarAPI
==========

API for the car expenses data

Slowly but surely transitioning to a full stack thing.
Currently Python backend with sqlite3, bottle server, javascript angular frontend and a d3 wrapper (dimple.js) for visualisations.
***
## Setting up the dev environment

**Create / Update the DB**
<br> Navigate to **_/backend/database_** and run **_python rebuild_db.py_** - this will create (or recreate) expenses.db based on the json data (data.json) located in the same folder.

**Install any dependencies**
<br>Navigate to the root folder and run **_pip install -r requirements.txt_** - this will install the python packages that the application depends on

**Running the application**
<br>Navigate to **_/backend_** and run **_python server.py_** - this will start the server at **localhost:8000**