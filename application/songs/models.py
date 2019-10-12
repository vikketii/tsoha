from application import db
from application.models import Base
from sqlalchemy.sql import text


class Song(Base):
    views = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=True)

    def __init__(self, name, album_id):
        self.name = name
        self.album_id = album_id
        self.views = 0

    @staticmethod
    def find_song_and_artists(id):
        stmt = text("""SELECT song.id, song.name, song.views,
                        artist.id, artist.name,
                        album.id, album.name FROM song
                        JOIN song_artist ON song_artist.song_id = song.id
                        JOIN artist ON artist.id = song_artist.artist_id
                        JOIN album ON album.id = song.album_id
                        WHERE song.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {'artists': []}

        for row in res:
            response.update(
                [('id', row[0]), ('name', row[1]), ('views', row[2]),
                ('album', {'id': row[5], 'name': row[6]})])
            response['artists'].append({'id': row[3], 'name': row[4]})

        return response
