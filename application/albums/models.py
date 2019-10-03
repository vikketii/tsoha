from application import db
from application.models import Base


class Album(Base):
    release_year = db.Column(db.Integer)

    songs = db.relationship('Song', backref='account', lazy=True)

    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
