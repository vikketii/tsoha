from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song
from application.songs.forms import SongForm
from application.artists.models import Artist
from application.albums.models import Album


@app.route('/songs/', methods=['GET'])
def songs_index():
    return render_template('songs/list.html', songs=Song.query.all())


@app.route('/songs/new/', methods=['GET'])
@login_required
def songs_form():
    form = SongForm()
    form.song_artist.choices = [(artist.id, artist.name)
                                for artist in Artist.query.order_by('name')]
    form.album.choices = [(artist.id, artist.name)
                          for artist in Album.query.order_by('name')]

    return render_template('songs/new.html', form=form)


@app.route('/songs/<song_id>/', methods=['GET'])
def songs_view_one(song_id):
    song = Song.query.get_or_404(song_id)
    song.views += 1
    db.session().commit()

    song_and_artists = Song.find_song_and_artists(song_id)

    return render_template('songs/one.html', song=song_and_artists)


@app.route('/songs/<song_id>/delete', methods=['POST'])
@login_required
def songs_delete_one(song_id):
    song = Song.query.get_or_404(song_id)

    db.session.delete(song)
    db.session.commit()

    return redirect(url_for('songs_index'))


@app.route('/songs/', methods=['POST'])
@login_required
def songs_create():
    form = SongForm(request.form)
    form.song_artist.choices = [(artist.id, artist.name)
                                for artist in Artist.query.order_by('name')]
    form.album.choices = [(artist.id, artist.name)
                          for artist in Album.query.order_by('name')]

    if not form.validate():
        return render_template('songs/new.html', form=form)

    song = Song(form.name.data, form.album.data)
    song.account_id = current_user.id

    artist = Artist.query.get(form.song_artist.data)
    artist.song_artist.append(song)

    album = Album.query.get(form.album.data)
    album.songs.append(song)

    db.session().add(song)
    db.session().add(artist)
    db.session().add(album)
    db.session().commit()

    return redirect(url_for('songs_index'))
