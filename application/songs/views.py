from application import app, db
from flask import redirect, render_template, request, url_for
from application.songs.models import Song

@app.route('/songs/', methods=['GET'])
def songs_index():
    return render_template('songs/list.html', songs=Song.query.all())

@app.route('/songs/new/')
def songs_form():
    return render_template('songs/new.html')

@app.route('/songs/<song_id>/', methods=['POST'])
def songs_add_view(song_id):
    s = Song.query.get(song_id)
    s.views += 1
    db.session().commit()

    return redirect(url_for('songs_index'))

@app.route('/songs/', methods=['POST'])
def songs_create():
    s = Song(request.form.get('name'))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for('songs_index'))