# **Welcome to Spooky Zephyr Warehouse! Your source for the most impressive inflatables this holiday season.**

(This is the final project for CS579, BU MET.)

**To get started, clone this repo.
`git clone https://github.com/katdob/SpookyZephyrWarehouse.git` and `cd SpookyZephyrWarehouse`.**

### Get the frontend up and running:

WIP! Check back later for updates.

### Get the backend up and running:

To begin, install [Python 3.8.3](https://www.python.org/).

Open a terminal and navigate to the backend directory with `cd backend`.
`python3 -m venv venv` to set up the virtual environment.
`source venv/bin/activate` to activate the virtual environment.
`python3 -m pip install -r requirements.txt` to download all the requirements.
Run `export FLASK_APP=app` to tell flask where the application is located.

In a new terminal window:
You'll need to have [MySQL](https://www.mysql.com/) installed and available at port 3306 on your machine. You can change this port to one you'd prefer to use later, when we define the database URI.

Get a MySQL repl going, and `create database SpookyZephyrWarehouse;`. Type `show databases;` to ensure that it's there and `exit;`.

Back in the backend terminal window:
Run `flask db upgrade` to run the data migrations and populate the database with the tables and columns as defined in `backend/app/models.py`.

Next, you'll populate the database by running `python3 seed_db.py`. You'll see printed output of what you've created with this script.

You'll need to have port 5000 available to run the development server. Run `flask run` to start the development server.

You should something like this:
(venv) your-computer-name:backend you$ flask run
 * Serving Flask app "app"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

 If you navigate to `http://127.0.0.1:5000/` in a browser, you'll see the text "Hello, World!".

 When you're done, you can simply `deactivate` to end the virtual environment.
