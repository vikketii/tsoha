from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ArtistForm(FlaskForm):
    name = StringField("Artist name", [validators.length(min=1, max=120)])

    class Meta:
        csrf = False