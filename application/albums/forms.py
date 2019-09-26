from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class AlbumForm(FlaskForm):
    name = StringField("Album name", [validators.length(min=1, max=120)])
    release_year = IntegerField("Release year")

    class Meta:
        csrf = False