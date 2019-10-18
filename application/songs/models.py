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
    def find_song_and_artists_and_samples(id):
        stmt = text("""SELECT song.id, song.name, song.views,
                        artist.id, artist.name,
                        album.id, album.name,
                        used.id, used_original.id, used_original.name,
                        original.id, original_used.id, original_used.name FROM song
                        JOIN song_artist ON song_artist.song_id = song.id
                        JOIN artist ON artist.id = song_artist.artist_id
                        JOIN album ON album.id = song.album_id
                        LEFT JOIN sample AS used ON used.used_id = song.id
                        LEFT JOIN song AS used_original ON used_original.id = used.original_id
                        LEFT JOIN sample AS original ON original.original_id = song.id
                        LEFT JOIN song AS original_used ON original_used.id = original.used_id
                        WHERE song.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {'artists': [], 'used_samples': [], 'original_samples': []}

        for row in res:
            response.update(
                [('id', row[0]), ('name', row[1]), ('views', row[2]),
                 ('album', {'id': row[5], 'name': row[6]})])
            response['artists'].append({'id': row[3], 'name': row[4]})

            if row[7] and row[8]:
                response['used_samples'].append({'id': row[7], 'original': {'id': row[8], 'name': row[9]}})
            if row[10] and row[11]:
                response['original_samples'].append({'id': row[10], 'used': {'id': row[11], 'name': row[12]}})

        return response

    @staticmethod
    def get_songs_and_sample_counts():
        stmt = text("""SELECT song.id, song.name,
                        COUNT(used.id), COUNT(original.id), song.views FROM song
                        LEFT JOIN sample AS used ON used.used_id = song.id
                        LEFT JOIN sample AS original ON original.original_id = song.id
                        GROUP BY song.id
                        ORDER BY song.views DESC
                        """)

        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({'id': row[0], 'name': row[1], 'samples_used_count': row[2],
                             'samples_made_count': row[3], 'views': row[4]})

        return response

    @staticmethod
    def get_song_artist(id):
        stmt = text("""SELECT artist.id FROM song
                        JOIN song_artist ON song_artist.song_id = song.id
                        JOIN artist ON artist.id = song_artist.artist_id
                        WHERE song.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = None

        for row in res:
            response = row[0]

        return response
