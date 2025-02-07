from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.length(min=3, max=120)])
    password = PasswordField('Password', [validators.length(min=2, max=120)])

    class Meta:
        csrf = False