from flask import render_template, request, redirect, url_for
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
        note_content = request.form.get("note_content")
        date_updated = datetime.utcnow()

        new_note = Note(
            title=title,
            description=description,
            note_content=note_content,
            date_updated=date_updated
        )

        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new_note.html")