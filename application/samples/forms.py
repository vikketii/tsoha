from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, validators


class SampleForm(FlaskForm):
    original = SelectField(
        'Sample origin', [validators.input_required()], coerce=int)
    used = SelectField(
        'Used in', [validators.input_required()], coerce=int)

    original_start = IntegerField('Sample starts at', [validators.number_range(min=0, max=1000)])
    used_start = IntegerField('Sample starts at', [validators.number_range(min=0, max=1000)])

    class Meta:
        csrf = False
