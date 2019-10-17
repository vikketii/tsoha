from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm


@app.route('/auth/signup', methods=['GET', 'POST'])
def auth_signup():
    if request.method == 'GET':
        return render_template('auth/signupform.html', form=SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template('auth/signupform.html', form=form)

    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template('auth/signupform.html', form=form, error='Username already taken')

    admin = not User.admin_exists()

    new_user = User(form.username.data, form.password.data, admin)

    db.session().add(new_user)
    db.session().commit()

    login_user(new_user)
    return redirect(url_for('index'))


@app.route('/auth/login', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'GET':
        return render_template('auth/loginform.html', form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data).first()

    if not user or not bcrypt.check_password_hash(user.password, form.password.data):
        return render_template('auth/loginform.html', form=form, error='No such username or password')

    login_user(user)
    return redirect(url_for('index'))


@app.route('/auth/logout')
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for('index'))
