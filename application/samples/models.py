from application import db
from sqlalchemy.sql import text
import datetime


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    original_id = db.Column(
        db.Integer, db.ForeignKey('song.id'), nullable=False)
    used_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

    original_start = db.Column(db.Integer, nullable=False)
    used_start = db.Column(db.Integer, nullable=False)

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
                        """)

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
                        original.id, original.name,
                        used.id, used.name FROM sample
                        JOIN song AS original ON original.id = sample.original_id
                        JOIN song AS used ON used.id = sample.used_id
                        WHERE sample.id = :id""").params(id=id)

        res = db.engine.execute(stmt)
        response = {'used': {'name': 'used_name'},
                    'original': {'name': 'original_name'}, 'views': 11}

        for row in res:
            response = {'id': row[0], 'views': row[1],
                        'original': {'id': row[2], 'name': row[3]},
                        'used': {'id': row[4], 'name': row[5]}}

        return response
