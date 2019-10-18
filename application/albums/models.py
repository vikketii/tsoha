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
                        song.id, song.name FROM album
                        LEFT JOIN song ON song.album_id = album.id
                        LEFT JOIN album_artist ON album_artist.album_id = album.id
                        LEFT JOIN artist ON artist.id = album_artist.artist_id
                        WHERE album.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {'artists': [], 'songs': []}

        added_artists = set()

        for row in res:
            response.update([('id', row[0]), ('name', row[1]),
                             ('release_year', row[2])])

            if row[3] and row[4] and row[3] not in added_artists:
                response['artists'].append({'id': row[3], 'name': row[4]})
                added_artists.add(row[3])

            if row[5] and row[6]:
                response['songs'].append({'id': row[5], 'name': row[6]})

        return response

    @staticmethod
    def get_album_with_most_samples():
        stmt = text("""SELECT counts.id, counts.name, counts.artist_id, counts.artist_name, MAX(counts.sample_count) FROM (
                        SELECT album.id AS id, album.name AS name,
                        artist.id AS artist_id, artist.name AS artist_name,
                        COUNT(sample.id) AS sample_count FROM album
                        LEFT JOIN song ON song.album_id = album.id
                        LEFT JOIN sample ON sample.used_id = song.id
                        LEFT JOIN album_artist ON album_artist.album_id = album.id
                        LEFT JOIN artist ON artist.id = album_artist.artist_id
                        GROUP BY album.id, artist.id) AS counts
                        """)


        res = db.engine.execute(stmt)
        response = {}

        for row in res:
            response = {'id': row[0], 'name': row[1], 'artist': {
                'id': row[2], 'name': row[3]}, 'samples_count': row[4]}

        return response
