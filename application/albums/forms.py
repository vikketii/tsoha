from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, validators
import datetime


class AlbumForm(FlaskForm):
    name = StringField("Album name", [validators.length(min=1, max=120)])
    album_artist = SelectField(
        u'Artist', [validators.input_required()], coerce=int)
    release_year = IntegerField("Release year", [validators.NumberRange(
        min=1800, max=datetime.datetime.now().year)])


    class Meta:
        csrf = False
