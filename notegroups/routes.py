from flask import render_template, request, redirect, url_for
from notegroups import app, db
from notegroups.models import Note, Tag
from datetime import datetime

#Home section
@app.route("/")
def home():
    #Search bar
    search_query = request.args.get('searching', '')
    #Search all notes against search input for matching words
    #in the title, description, and tag section
    if search_query:
         notes = Note.query.join(Tag).filter(
        (Note.title.ilike(f'%{search_query}%')) | 
        (Note.description.ilike(f'%{search_query}%')) |
        (Tag.name.ilike(f'%{search_query}%'))
        ).order_by(Note.date_updated.desc()).all()
    else:
        #If not doing a search, then dispaly all
        notes=list(Note.query.order_by(Note.date_updated.desc()).all())
    return render_template("home.html", notes=notes)

#New note
@app.route("/new_note", methods=["GET","POST"])
def new_note():
    if request.method=="POST":
        #If user submits data, grab data
        title = request.form.get("title")
        description = request.form.get("description")
        note_content = request.form.get("note_content")
        tag_name = request.form.get("tag")
        date_updated = datetime.utcnow()

        #Check if tag exists already, if not, create it
        tag = Tag.query.filter_by(name=tag_name).first()
        if not tag:
            tag=Tag(name=tag_name)
            db.session.add(tag)
            db.session.commit()

        #Fill database with grabbed data
        new_note = Note(
            title=title,
            description=description,
            note_content=note_content,
            date_updated=date_updated,
            tag_id=tag.id
        )

        #Save data
        db.session.add(new_note)
        db.session.commit()
        #Redirect user back to homepage
        return redirect(url_for("home"))
    return render_template("new_note.html")

#Edit note
@app.route("/edit_note/<int:note_id>", methods=["GET","POST"])
def edit_note(note_id):

    #Check if post exists or give a 404
    note=Note.query.get_or_404(note_id)

    #If user submits data then rewrite saved data with new data
    if request.method=="POST":
        note.title=request.form.get("title")
        note.description=request.form.get("description")
        tag_name = request.form.get("tag")
        note.date_updated=datetime.utcnow()

        #Check if edited tag exists already, if not, create it
        tag = Tag.query.filter_by(name=tag_name).first()
        if not tag:
            tag=Tag(name=tag_name)
            db.session.add(tag)
            db.session.commit()

        db.session.commit()
        #Redirect user back home
        return redirect(url_for("home"))
    return render_template("edit_note.html", note=note)

#Delete note
@app.route("/delete_note/<int:note_id>")
def delete_note(note_id):
    note=Note.query.get_or_404(note_id)

    #Delete the note
    db.session.delete(note)
    db.session.commit()
    #Redirect user back home
    return redirect(url_for("home"))

#Note content
@app.route("/note/<int:note_id>", methods=["GET", "POST"])
def note(note_id):
    note = Note.query.get_or_404(note_id)

    #Update file time on open
    note.date_updated = datetime.utcnow()

    if request.method == "POST":
        # Collect note content
        note.note_content = request.form.get("content")
        
        # Update the file time on saving
        note.date_updated = datetime.utcnow()
        
        # Commit the changes to the database
        db.session.commit()

        # Redirect to the same note page after saving
        return redirect(url_for('note', note_id=note.id))

    # Update the time when the note is opened (GET request)
    note.date_updated = datetime.utcnow()
    db.session.commit()

    return render_template("note.html", note=note)