from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.artists.models import Artist
from application.artists.forms import ArtistForm

@app.route('/artists/', methods=['GET'])
def artists_index():
    return render_template('artists/list.html', artists=Artist.query.all())

@app.route('/artists/new/')
@login_required
def artists_form():
    return render_template('artists/new.html', form=ArtistForm())

@app.route('/artists/<artist_id>/', methods=['GET'])
def artists_view_one(artist_id):
    a = Artist.query.get(artist_id)
    return render_template('artists/one.html', artist=a)

@app.route('/artists/', methods=['POST'])
@login_required
def artists_create():
    form = ArtistForm(request.form)

    if not form.validate():
        return render_template('artists/new.html', form = form)

    a = Artist(form.name.data)
    db.session().add(a)
    db.session().commit()

    return redirect(url_for('artists_index'))