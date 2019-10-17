from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text

song_artist = db.Table('song_artist',
                       db.Column('artist_id', db.Integer, db.ForeignKey(
                           'artist.id'), primary_key=True),
                       db.Column('song_id', db.Integer, db.ForeignKey(
                           'song.id'), primary_key=True)
                       )

album_artist = db.Table('album_artist',
                        db.Column('artist_id', db.Integer, db.ForeignKey(
                            'artist.id'), primary_key=True),
                        db.Column('album_id', db.Integer, db.ForeignKey(
                            'album.id'), primary_key=True)
                        )


class Artist(Base):
    song_artist = db.relationship(
        'Song', secondary=song_artist, backref=db.backref('artists', lazy='dynamic'))
    album_artist = db.relationship(
        'Album', secondary=album_artist, backref=db.backref('artists', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_artists_and_song_counts():
        stmt = text('''SELECT artist.id, artist.name, COUNT(song.id) AS song_count FROM Artist
                        LEFT JOIN song_artist AS song_artist_1 ON artist.id = song_artist_1.artist_id
                        LEFT JOIN song ON song.id = song_artist_1.song_id
                        GROUP BY artist.id
                        ''')

        response = db.engine.execute(stmt)
        return response

    @staticmethod
    def find_artist_and_all_albums_and_songs(id):
        stmt = text('''SELECT artist.id, artist.name,
                        album.id, album.name,
                        COUNT(song.id) FROM Artist
                        LEFT JOIN album_artist ON album_artist.artist_id = artist.id
                        LEFT JOIN album ON album.id = album_artist.album_id
                        LEFT JOIN song ON song.album_id = album.id
                        WHERE artist.id = :id
                        GROUP BY album.id
                        ''').params(id=id)

        res = db.engine.execute(stmt)
        response = {'albums': []}


        for row in res:
            response.update([('id', row[0]), ('name', row[1])])

            if row[2]:
                response['albums'].append({'id': row[2], 'name': row[3], 'song_count': row[4]})

        return response
