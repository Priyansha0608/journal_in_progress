from flask import Flask, render_template

app = Flask(__name__)

@app.route("/page")
def page():
    return render_template("index.html")