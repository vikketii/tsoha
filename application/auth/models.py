from application import db, bcrypt
from sqlalchemy.sql import text


class User(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    date_created = db.Column(
        db.DateTime(), default=db.func.current_timestamp(), nullable=False)
    songs = db.relationship('Song', backref='account_songs', lazy=True)

    def __init__(self, username, password, admin):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.admin = admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ['ADMIN']

    @staticmethod
    def admin_exists():
        stmt = text("""SELECT account.id From account
                        WHERE account.admin = True""")

        res = db.engine.execute(stmt)
        response = None

        for row in res:
            response = row[0]

        return response