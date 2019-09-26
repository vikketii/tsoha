from application import db
from application.models import Base
from ..artists.models import song_artist, Artist

from sqlalchemy.sql import text


class Song(Base):
    views = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=True)

    song_artist = db.relationship(
        'Artist', secondary=song_artist, backref=db.backref('songs', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
        self.views = 0

    @staticmethod
    def find_song_and_artists(id):
        stmt = text("""SELECT song.name AS song_name, song.views AS song_views,
                        artist.name AS artist_name FROM song
                        JOIN song_artist AS song_artist_1 ON song.id = song_artist_1.song_id
                        JOIN artist ON artist.id = song_artist_1.artist_id
                        WHERE song.id = :id""").params(id=id)

        # res = db.session.query(Song, Artist).filter(
        #     Song.id == id).join(Artist, Song.song_artist).all()
        # for s, a in res:
        #     print(s.name, a.name)

        res = db.engine.execute(stmt)
        for row in res:
            response = {"name": row[0], "views":row[1], "artists":row[2]}

        return response
