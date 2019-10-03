from application import db
from application.models import Base
from sqlalchemy.sql import text


class Song(Base):
    views = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=True)

    def __init__(self, name):
        self.name = name
        self.views = 0

    @staticmethod
    def find_song_and_artists(id):
        stmt = text("""SELECT song.id, song.name, song.views, artist.id, artist.name FROM song
                        JOIN song_artist ON song.id = song_artist.song_id
                        JOIN artist ON artist.id = song_artist.artist_id
                        WHERE song.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {'artists': []}
        for row in res:
            response.update(
                [('id', row[0]), ('name', row[1]), ('views', row[2])])
            response['artists'].append({'id': row[3], 'name': row[4]})

        return response
