from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text

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

    @staticmethod
    def get_artists_and_song_counts():
        stmt = text("""SELECT artist.id, artist.name, COUNT(song.id) AS song_count FROM Artist
                        LEFT JOIN song_artist AS song_artist_1 ON artist.id = song_artist_1.artist_id
                        LEFT JOIN song ON song.id = song_artist_1.song_id
                        GROUP BY artist.id
                        """)

        response = db.engine.execute(stmt)
        return response

    @staticmethod
    def find_artist_and_all_songs(id):
        stmt = text("""SELECT artist.name AS artist_name, song.name AS song_name FROM Artist
                        LEFT JOIN song_artist AS song_artist_1 ON artist.id = song_artist_1.artist_id
                        LEFT JOIN song ON song.id = song_artist_1.song_id
                        WHERE artist.id = :id
                        """).params(id=id)

        res = db.engine.execute(stmt)
        response = {"name": '', "songs": [], "count": 0}
        for row in res:
            response['name'] = row[0]
            response['songs'].append(row[1])
            response['count'] += 1

        return response
