from application import db
from application.models import Base
from sqlalchemy.sql import text


class Album(Base):
    release_year = db.Column(db.Integer)
    songs = db.relationship('Song', backref='album', lazy=True)

    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    @staticmethod
    def find_album_artist_and_songs(id):
        stmt = text("""SELECT album.id, album.name, album.release_year,
                        artist.id, artist.name,
                        song.id, song.name FROM song
                        JOIN album ON album.id = song.album_id
                        JOIN album_artist ON album_artist.album_id = album.id
                        JOIN artist ON artist.id = album_artist.artist_id
                        WHERE album.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {'artists': [], 'songs': []}

        for row in res:
            response.update([('id', row[0]), ('name', row[1]),
                             ('release_year', row[2])])
            response['artists'].append({'id': row[3], 'name': row[4]})
            response['songs'].append({'id': row[5], 'name': row[6]})

        return response
