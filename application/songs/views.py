from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song
from application.songs.forms import SongForm
from application.artists.models import Artist

@app.route('/songs/', methods=['GET'])
def songs_index():
    return render_template('songs/list.html', songs=Song.query.all())

@app.route('/songs/new/', methods=['GET'])
@login_required
def songs_form():
    form = SongForm()
    form.song_artist.choices = [(a.id, a.name) for a in Artist.query.order_by('name')]
    return render_template('songs/new.html', form=form)

@app.route('/songs/<song_id>/', methods=['GET'])
def songs_view_one(song_id):
    s = Song.query.get(song_id)
    s.views += 1
    db.session().commit()

    song_and_artist = Song.find_song_and_artists(song_id)

    print('//------')
    print(song_and_artist)
    print('------>>')


    return render_template('songs/one.html', song=song_and_artist)

@app.route('/songs/<song_id>/', methods=['POST'])
def songs_add_view(song_id):
    s = Song.query.get(song_id)
    s.views += 1
    db.session().commit()

    return redirect(url_for('songs_index'))

@app.route('/songs/', methods=['POST'])
@login_required
def songs_create():
    form = SongForm(request.form)

    # if not form.validate():
    #     return render_template('songs/new.html', form = form)

    s = Song(form.name.data)
    s.account_id = current_user.id

    s.song_artist = [ Artist.query.get(form.song_artist.data) ]

    db.session().add(s)
    db.session().commit()

    return redirect(url_for('songs_index'))