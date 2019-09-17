from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SongForm(FlaskForm):
    name = StringField("Song name", [validators.length(min=1)])

    class Meta:
        csrf = False