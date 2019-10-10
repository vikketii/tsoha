from flask_wtf import FlaskForm
from wtforms import TimeField, SelectField, validators


class SampleForm(FlaskForm):
    original = SelectField(
        'Sample origin', [validators.input_required()], coerce=int)
    used = SelectField(
        'Used in', [validators.input_required()], coerce=int)

    original_start = TimeField('Sample starts at', format='%M:%S')
    used_start = TimeField('Sample starts at', format='%M:%S')

    class Meta:
        csrf = False
