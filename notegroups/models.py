from notegroups import db


class Note(db.Model):
    # Schema for the note model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    note_content = db.Column(db.Text, nullable=False)
    date_updated = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now(),
        onupdate=db.func.now())
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=True)

    tag = db.relationship('Tag', backref='notes', lazy=True)

    def __repr__(self):
        return f"Note{self.id} - {self.title} - {self.description}"


class Tag(db.Model):
    # Tags schema for note model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Tag {self.id} - {self.name}"
