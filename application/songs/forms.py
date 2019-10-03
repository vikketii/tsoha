from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators


class SongForm(FlaskForm):
    name = StringField("Song name", [validators.length(min=1, max=120)])
    song_artist = SelectField(
        u'Artist', [validators.input_required()], coerce=int)

    class Meta:
        csrf = False
