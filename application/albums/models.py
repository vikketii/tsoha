from application import db
from application.models import Base
from ..artists.models import album_artist, Artist

class Album(Base):
    release_year = db.Column(db.Integer)

    album_artist = db.relationship('Artist', secondary=album_artist, backref=db.backref('albums', lazy='dynamic'))
    songs = db.relationship('Song', backref='account', lazy=True)

    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year