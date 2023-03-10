# to activate venv MAC USERS use source journal_venv/Scripts/activate
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page():
    return render_template("index.html")