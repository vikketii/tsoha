from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref

song_artist = db.Table('song_artist',
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.PrimaryKeyConstraint('artist_id', 'song_id')
)

album_artist = db.Table('album_artist',
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),
    db.PrimaryKeyConstraint('artist_id', 'album_id')
)

class Artist(Base):

    song_artist = db.relationship('Song', secondary=song_artist, backref=db.backref('artists', lazy='dynamic'))
    album_artist = db.relationship('Album', secondary=album_artist, backref=db.backref('artists', lazy='dynamic'))

    def __init__(self, name):
        self.name = name