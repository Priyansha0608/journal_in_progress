# to activate venv MAC USERS use source journal_venv/Scripts/activate
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func # to access SQL Functions like date and time when record is created 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # specify which database you want to connect to
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # tracking midifications of objects; set to false to use less memory

journal_db = SQLAlchemy(app) # to connect Flask application w SQLAlchemy and store database object
initialized = False
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

    #Not a necessary function but can be helpful for debugging purposes
    def __repr__(self) -> str:
        return f"Element: {self.type_element} Coordinates {self.l},{self.t}"

# NEXT STEP: create function to initialize canvas from database
def initialize_canvas():
    """Will only happen the first time when canvas is not 'initialized'
    and will drop any existing tables."""
    with app.app_context():
        journal_db.drop_all()
        journal_db.create_all()


@app.route("/") # app.route is the url that runs a defined function, in this case page
def page():
    global initialized
    if initialized == False:
        initialize_canvas()
        initialized = True
    return render_template("index.html")

# canvas.js creates a HTML form request to trigger this function 
@app.route("/getElement", methods=["POST"])
def getElement():
    """Receives information from canvas.js and sends it to update the
    database and canvas"""
    id = request.form.get("id")
    type_element = request.form.get("type_element")
    w = request.form.get("w")
    t = request.form.get("t")
    l = request.form.get("l")
    txt = request.form.get("txt")

    update_canvas(id, type_element, w, t, l, txt)
    return [id, type_element, w, t, l, txt]

# add element to the database 
def update_canvas(id, type_element, width, top, left, text):
    #checks to see if the element already exists
    e = Element.query.filter_by(id = id).first() #will return None if does not exist
    #query.filter_by will return a list of all elements that fit the criteria
    #.first() checks the first element in that list 
    # (without would be comparing [] != None which would always be true)
    if e != None:
        print("element is modified!")
        e.w = width
        e.t = top
        e.l = left
        e.txt = text
    else:
        e = Element(id = id, type_element=type_element, w=width,t=top, l=left, txt=text)
        journal_db.session.add(e)
    
    journal_db.session.commit()
    print(Element.query.all())