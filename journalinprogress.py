# to activate venv MAC USERS use source journal_venv/Scripts/activate
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func # to access SQL Functions like date and time when record is created 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # specify which database you want to connect to
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # tracking midifications of objects; set to false to use less memory

journal_db = SQLAlchemy(app) # to connect Flask application w SQLAlchemy and store database object

# journal_db variable is how we interact with the database
class Element(journal_db.Model):
    # so far only element: textbox
    #   - type, width, left, top, text
    id = journal_db.Column(journal_db.Integer, primary_key = True)
    type_element = journal_db.Column(journal_db.Text)
    w = journal_db.Column(journal_db.Float)
    l = journal_db.Column(journal_db.Float)
    t = journal_db.Column(journal_db.Float)
    txt = journal_db.Column(journal_db.Text)

# NEXT STEP: create function to initialize canvas from database

@app.route("/") # app.route is the url that runs a defined function, in this case page
def page():
    return render_template("index.html")
