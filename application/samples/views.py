from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.samples.models import Sample
from application.samples.forms import SampleForm
from application.songs.models import Song


@app.route('/samples/', methods=['GET'])
def samples_index():
    return render_template('samples/list.html', samples=Sample.get_samples_and_songs())


@app.route('/samples/new/', methods=['GET'])
@login_required
def samples_form():
    form = SampleForm()
    songs = [(song.id, song.name) for song in Song.query.order_by('name')]
    form.original.choices = songs
    form.used.choices = songs
    return render_template('samples/new.html', form=form)


@app.route('/samples/<sample_id>/', methods=['GET'])
def samples_view_one(sample_id):
    s = Sample.query.get_or_404(sample_id)
    s.views += 1
    db.session().commit()

    sample_and_songs = Sample.find_sample_and_songs(sample_id)

    return render_template('samples/one.html', sample=sample_and_songs)


@app.route('/samples/<sample_id>/delete', methods=['POST'])
@login_required
def samples_delete_one(sample_id):
    s = Sample.query.get_or_404(sample_id)

    if s.account_id != current_user.id:
        return redirect(url_for('samples_view_one', sample_id=sample_id))

    db.session.delete(s)
    db.session.commit()

    return redirect(url_for('samples_index'))


@app.route('/samples/', methods=['POST'])
@login_required
def samples_create():
    form = SampleForm(request.form)

    songs = [(song.id, song.name) for song in Song.query.order_by('name')]
    form.original.choices = songs
    form.used.choices = songs

    if not form.validate():
        return render_template('samples/new.html', form=form)

    s = Sample(form.original.data, form.used.data, form.original_start.data,
               form.used_start.data, current_user.id)

    db.session().add(s)
    db.session().commit()

    return redirect(url_for('samples_index'))


@app.route('/samples/<sample_id>/edit', methods=['GET'])
@login_required
def samples_edit_one(sample_id):
    sample = Sample.query.get_or_404(sample_id)

    if sample.account_id != current_user.id:
        return redirect(url_for('samples_view_one', sample_id=sample_id))

    form = SampleForm(request.form)
    songs = [(song.id, song.name) for song in Song.query.order_by('name')]
    form.original.choices = songs
    form.used.choices = songs

    form.original.data = sample.original_id
    form.used.data = sample.used_id
    form.original_start.data = sample.original_start
    form.used_start.data = sample.used_start

    return render_template('samples/update.html', form=form, sample_id=sample_id)

@app.route('/samples/<sample_id>/edit', methods=['POST'])
@login_required
def samples_update_one(sample_id):
    form = SampleForm(request.form)
    songs = [(song.id, song.name) for song in Song.query.order_by('name')]
    form.original.choices = songs
    form.used.choices = songs

    if not form.validate():
        return render_template('samples/new.html', form=form)

    sample = Sample.query.get_or_404(sample_id)

    if sample.account_id != current_user.id:
        return redirect(url_for('samples_view_one', sample_id=sample_id))

    sample.original_id = form.original.data
    sample.used_id = form.used.data
    sample.original_start = form.original_start.data
    sample.used_start = form.used_start.data

    db.session.commit()

    return redirect(url_for('samples_view_one', sample_id=sample_id))