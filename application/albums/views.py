from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.albums.models import Album
from application.albums.forms import AlbumForm
from application.artists.models import Artist

@app.route('/albums/', methods=['GET'])
def albums_index():
    return render_template('albums/list.html', albums=Album.query.all())

@app.route('/albums/new/')
@login_required
def albums_form():
    form = AlbumForm()
    form.album_artist.choices = [(a.id, a.name)
                                for a in Artist.query.order_by('name')]
    return render_template('albums/new.html', form=form)

@app.route('/albums/<album_id>/', methods=['GET'])
def albums_view_one(album_id):
    a = Album.query.get(album_id)
    return render_template('albums/one.html', album=a)

@app.route('/albums/', methods=['POST'])
@login_required
def albums_create():
    form = AlbumForm(request.form)

    album = Album(form.name.data, form.release_year.data)

    artist = Artist.query.get(form.album_artist.data)
    artist.album_artist.append(album)

    db.session().add(album)
    db.session().add(artist)
    db.session().commit()

    return redirect(url_for('albums_index'))