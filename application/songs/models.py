from application import db
from ..artists.models import song_artist, Artist


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    views = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    song_artist = db.relationship('Artist', secondary=song_artist, backref=db.backref('songs', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
        self.views = 0