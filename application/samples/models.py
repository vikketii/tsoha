from application import db
from sqlalchemy.sql import text
import datetime


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    original_id = db.Column(
        db.Integer, db.ForeignKey('song.id'), nullable=False)
    used_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

    original_start = db.Column(db.Time, nullable=False)
    used_start = db.Column(db.Time, nullable=False)

    views = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)

    date_created = db.Column(
        db.DateTime(), default=db.func.current_timestamp(), nullable=False)

    def __init__(self, original_id, used_id, original_start, used_start, account_id):
        self.original_id = original_id
        self.used_id = used_id
        self.original_start = original_start
        self.used_start = used_start
        self.account_id = account_id
        self.views = 0

    @staticmethod
    def get_samples_and_songs():
        stmt = text("""SELECT sample.id, sample.views,
                        original.id, original.name,
                        used.id, used.name FROM sample
                        JOIN song AS original ON original.id = sample.original_id
                        JOIN song AS used ON used.id = sample.used_id
                        ORDER BY sample.views DESC
                        """)

        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({'id': row[0], 'views': row[1],
                             'original': {'id': row[2], 'name': row[3]},
                             'used': {'id': row[4], 'name': row[5]}})

        return response

    @staticmethod
    def get_samples_and_songs_owned(user_id):
        stmt = text("""SELECT sample.id, sample.views,
                        original.id, original.name,
                        used.id, used.name FROM sample
                        JOIN song AS original ON original.id = sample.original_id
                        JOIN song AS used ON used.id = sample.used_id
                        WHERE sample.account_id = :user_id
                        ORDER BY sample.views DESC
                        """).params(user_id=user_id)

        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({'id': row[0], 'views': row[1],
                             'original': {'id': row[2], 'name': row[3]},
                             'used': {'id': row[4], 'name': row[5]}})

        return response

    @staticmethod
    def find_sample_and_songs(id):
        stmt = text("""SELECT sample.id, sample.views,
                        original.id, original.name, sample.original_start,
                        used.id, used.name, sample.used_start,
                        account.username, account.id FROM sample
                        JOIN song AS original ON original.id = sample.original_id
                        JOIN song AS used ON used.id = sample.used_id
                        JOIN account ON account.id = sample.account_id
                        WHERE sample.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {}

        for row in res:
            orig_time = row[4]
            used_time = row[7]
            if type(orig_time) is str:
                orig_time = datetime.datetime.strptime(
                    orig_time, '%H:%M:%S.%f')
                used_time = datetime.datetime.strptime(
                    used_time, '%H:%M:%S.%f')

            response = {'id': row[0], 'views': row[1], 'account': row[8], 'account_id': row[9],
                        'original': {'id': row[2], 'name': row[3], 'start': orig_time},
                        'used': {'id': row[5], 'name': row[6], 'start': used_time}}

        return response

    @staticmethod
    def get_most_recent():
        stmt = text("""SELECT sample.id, MAX(sample.date_created), sample.views,
                        original.id, original.name,
                        used.id, used.name FROM sample
                        JOIN song AS original ON original.id = sample.original_id
                        JOIN song AS used ON used.id = sample.used_id
                        GROUP BY sample.id
                        """)

        res = db.engine.execute(stmt)
        response = {}

        for row in res:
            response = {'id': row[0], 'time': row[1], 'views': row[2], 'original': {
                'id': row[3], 'name': row[4]}, 'used': {'id': row[5], 'name': row[6]}}

        return response
