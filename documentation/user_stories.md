# User stories

## As a normal user, I want to

### see the most recently added sample
<pre><code>
SELECT sample.id, MAX(sample.date_created), sample.views,
original.id, original.name,
used.id, used.name FROM sample
JOIN song AS original ON original.id = sample.original_id
JOIN song AS used ON used.id = sample.used_id
GROUP BY sample.id, original.id, used.id
</code></pre>

### see album using most samples
<pre><code>
SELECT counts.id, counts.name, counts.artist_id, counts.artist_name, counts.sample_count FROM (
SELECT album.id AS id, album.name AS name,
artist.id AS artist_id, artist.name AS artist_name,
COUNT(sample.id) AS sample_count FROM album
LEFT JOIN song ON song.album_id = album.id
LEFT JOIN sample ON sample.used_id = song.id
LEFT JOIN album_artist ON album_artist.album_id = album.id
LEFT JOIN artist ON artist.id = album_artist.artist_id
GROUP BY album.id, artist.id) AS counts
ORDER BY counts.sample_count DESC
</code></pre>

### view all samples and list them in the order of most views
<pre><code>
SELECT sample.id, sample.views,
original.id, original.name,
used.id, used.name FROM sample
JOIN song AS original ON original.id = sample.original_id
JOIN song AS used ON used.id = sample.used_id
WHERE sample.account_id = :user_id
ORDER BY sample.views DESC
</code></pre>

### view single sample and it's original song and where it's used in
<pre><code>
SELECT sample.id, sample.views,
original.id, original.name, sample.original_start,
used.id, used.name, sample.used_start,
account.username, account.id FROM sample
JOIN song AS original ON original.id = sample.original_id
JOIN song AS used ON used.id = sample.used_id
JOIN account ON account.id = sample.account_id
WHERE sample.id = :id
</code></pre>


### view info about one song and see all the samples used in it and made out of it
<pre><code>
SELECT song.id, song.name, song.views,
artist.id, artist.name,
album.id, album.name,
used.id, used_original.id, used_original.name,
original.id, original_used.id, original_used.name FROM song
JOIN song_artist ON song_artist.song_id = song.id
JOIN artist ON artist.id = song_artist.artist_id
JOIN album ON album.id = song.album_id
LEFT JOIN sample AS used ON used.used_id = song.id
LEFT JOIN song AS used_original ON used_original.id = used.original_id
LEFT JOIN sample AS original ON original.original_id = song.id
LEFT JOIN song AS original_used ON original_used.id = original.used_id
WHERE song.id = :id
</code></pre>

### view all artist's albums and show how many songs there are in the database for each album
<pre><code>
SELECT artist.id, artist.name,
album.id, album.name,
COUNT(song.id) FROM Artist
LEFT JOIN album_artist ON album_artist.artist_id = artist.id
LEFT JOIN album ON album.id = album_artist.album_id
LEFT JOIN song ON song.album_id = album.id
WHERE artist.id = :id
GROUP BY artist.id, album.id
</code></pre>

## As a logged in user, I want to do all of the above and

### add new sample
<pre><code>
INSERT INTO sample
(original_id, used_id, original_start, used_start, views, account_id, date_created)
VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
</code></pre>

### see all samples I own
<pre><code>
SELECT sample.id, sample.views,
original.id, original.name,
used.id, used.name FROM sample
JOIN song AS original ON original.id = sample.original_id
JOIN song AS used ON used.id = sample.used_id
WHERE sample.account_id = :user_id
ORDER BY sample.views DESC
</code></pre>

### edit and remove a sample that I own

## As an admin, I want to do all of the above and

### edit and remove samples and songs even if I don't own them