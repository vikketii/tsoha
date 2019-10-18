# User Instructions

## 1. Creating an account
Create account at [https://thawing-coast-05641.herokuapp.com/auth/signup](https://thawing-coast-05641.herokuapp.com/auth/signup). Username has to be unique.

## 2. Logging in
After creating account, user is automatically logged in. You can also login at [https://thawing-coast-05641.herokuapp.com/auth/login](https://thawing-coast-05641.herokuapp.com/auth/login).

## 3. Index page
Shows information of the database, if there is any samples added. Shows the most recent sample added and also the album using most samples.

## 4. Adding information
Adding information requires account. After logging in, user can see 'Add' item in navigation bar.
### 1. Sample
[https://thawing-coast-05641.herokuapp.com/samples/new/](https://thawing-coast-05641.herokuapp.com/samples/new/)
Adding sample requires information about the original song and the usage of the sample and time it starts at. Time is added in 'mm:ss' format. If the original song or the song using the sample is not in the database, user can add it by clicking the 'Add song!' link.

### 2. Song
[https://thawing-coast-05641.herokuapp.com/songs/new/](https://thawing-coast-05641.herokuapp.com/songs/new/)
User can add song by giving the songs name and artist. If the artist is not in the database, user can add it by clicking the 'Add missing artist!' link.

### 3. Album
[https://thawing-coast-05641.herokuapp.com/albums/new/](https://thawing-coast-05641.herokuapp.com/albums/new/)
User can add album by giving the albums name, artist and release year. If the artist is not in the database, user can add it by clicking the 'Add missing artist!' link. Release year is limited between 1800 and current year.

### 4. Artist
[https://thawing-coast-05641.herokuapp.com/artists/new/](https://thawing-coast-05641.herokuapp.com/artists/new/)
Adding artist requires only artist name.

## 5. Lists
Lists are available for everyone. There are 4 different lists(samples, songs, artists, albums) that give summaries about the database. Each list contains links to pages containing single item.

## 6. Single items
Pages for single items in the database.
### 1. Sample
Contains information about single sample. The page tells where the sample is used, what is its origin and what time user can hear the sample in the songs. Page also tells how many times the page has been visited, and who is the owner of the page. If user is logged in as the page owner, deleting and editing the sample becomes available. Admin can also do these edits.

### 2. Song
Shows title, artist and album of the song. Admin user can also edit and delete single song.

### 3. Album
Shows album name, artists, release year and lists all the songs in the album.

### 4. Artist
Shows artist name, how many albums they have and lists all albums and song counts in them.

## 7. Owned samples
Page lists all the samples user owns and can edit. If the user is admin, shows all samples.
