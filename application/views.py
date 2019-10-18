from flask import render_template
from application import app

from application.samples.models import Sample
from application.albums.models import Album

@app.route("/")
def index():
    most_recent_sample = Sample.get_most_recent()
    album_with_most_samples = Album.get_album_with_most_samples()


    print('<-----')
    print(most_recent_sample)
    print(album_with_most_samples)
    print('<-----')
    return render_template('index.html', most_recent_sample=most_recent_sample, album_with_most_samples=album_with_most_samples)
