from flask import render_template, request, redirect, url_for
from notegroups import app, db
from notegroups.models import Note
from datetime import datetime

@app.route("/")
def home():
    notes=list(Note.query.order_by(Note.date_updated.desc()).all())
    return render_template("home.html", notes=notes)

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

@app.route("/edit_note/<int:note_id>", methods=["GET","POST"])
def edit_note(note_id):
    note=Note.query.get_or_404(note_id)

    if request.method=="POST":
        note.title=request.form.get("title")
        note.description=request.form.get("description")
        note.date_updated=datetime.utcnow()
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_note.html", note=note)

@app.route("/delete_note/<int:note_id>")
def delete_note(note_id):
    note=Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("home"))