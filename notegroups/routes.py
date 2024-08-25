from flask import render_template, request, url_for
from notegroups import app, db
from notegroups.models import Note

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/note")
def note():
    return render_template("note.html")

@app.route("/new_note", methods=["GET","POST"])
def new_note():
    if request.method=="POST":
        title = request.form.get("title")
        description = request.form.get("description")
        date_updated = datetime.utcnow()

        new_note = Note(title=title, description=description, date_updated=date_updated)
    return render_template("new_note.html")