from application import db
from application.models import Base
from ..artists.models import song_artist, Artist


class Song(Base):
    views = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

    song_artist = db.relationship('Artist', secondary=song_artist, backref=db.backref('songs', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
        self.views = 0