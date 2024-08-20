from flask import render_template
from notegroups import app, db
from notegroups.models import Note

@app.route("/")
def home():
    return render_template("home.html")