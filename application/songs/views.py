from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.songs.models import Song
from application.songs.forms import SongForm

@app.route('/songs/', methods=['GET'])
def songs_index():
    return render_template('songs/list.html', songs=Song.query.all())

@app.route('/songs/new/')
@login_required
def songs_form():
    return render_template('songs/new.html', form=SongForm())

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

    if not form.validate():
        return render_template('songs/new.html', form = form)

    s = Song(form.name.data)
    s.account_id = current_user.id

    db.session().add(s)
    db.session().commit()

    return redirect(url_for('songs_index'))