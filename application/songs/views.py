from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song
from application.songs.forms import SongForm, SongUpdateForm
from application.artists.models import Artist
from application.albums.models import Album


@app.route('/songs/', methods=['GET'])
def songs_index():
    return render_template('songs/list.html', songs=Song.get_songs_and_sample_counts())


@app.route('/songs/new/', methods=['GET'])
@login_required
def songs_form():
    form = SongForm()
    form.song_artist.choices = [(artist.id, artist.name)
                                for artist in Artist.query.order_by('name')]
    form.album.choices = [(album.id, album.name)
                          for album in Album.query.order_by('name')]

    return render_template('songs/new.html', form=form)


@app.route('/songs/<song_id>/', methods=['GET'])
def songs_view_one(song_id):
    song = Song.query.get_or_404(song_id)
    song.views += 1
    db.session().commit()

    song_and_artists_and_samples = Song.find_song_and_artists_and_samples(song_id)

    return render_template('songs/one.html', song=song_and_artists_and_samples)


@app.route('/songs/<song_id>/delete', methods=['POST'])
@login_required
def songs_delete_one(song_id):
    if not current_user.admin:
        redirect(url_for('songs_index'))

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
    form.album.choices = [(album.id, album.name)
                          for album in Album.query.order_by('name')]

    if not form.validate():
        return render_template('songs/new.html', form=form)

    song = Song(form.name.data, form.album.data)
    song.account_id = current_user.id

    artist = Artist.query.get(form.song_artist.data)
    artist.song_artist.append(song)

    db.session().add(song)
    db.session().add(artist)
    db.session().commit()

    return redirect(url_for('songs_index'))


@app.route('/songs/<song_id>/edit', methods=['GET'])
@login_required
def songs_edit_one(song_id):
    if not current_user.admin:
        return redirect(url_for('songs_view_one', song_id=song_id))

    song = Song.query.get_or_404(song_id)

    form = SongUpdateForm(request.form)
    form.album.choices = [(album.id, album.name)
                          for album in Album.query.order_by('name')]

    form.name.data = song.name
    form.album.data = song.album_id

    return render_template('songs/update.html', form=form, song_id=song_id)


@app.route('/songs/<song_id>/edit', methods=['POST'])
@login_required
def songs_update_one(song_id):
    if not current_user.admin:
        return redirect(url_for('songs_view_one', song_id=song_id))

    form = SongUpdateForm(request.form)
    form.album.choices = [(album.id, album.name)
                          for album in Album.query.order_by('name')]

    if not form.validate():
        return render_template('songs/update.html', form=form, song_id=song_id)

    song = Song.query.get_or_404(song_id)
    song.name = form.name.data
    song.album_id = form.album.data

    db.session.commit()

    return redirect(url_for('songs_view_one', song_id=song_id))
