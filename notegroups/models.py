from notegroups import db

class Note(db.Model):
    #Schema for the note model
    id = db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    note_content = db.Column(db.Text, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return self