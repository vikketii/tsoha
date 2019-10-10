# User Instructions

1. Creating an account
Create account at [https://thawing-coast-05641.herokuapp.com/auth/signup](https://thawing-coast-05641.herokuapp.com/auth/signup). Username has to be unique.

2. Logging in
After creating account, user is automatically logged in. You can also login at [https://thawing-coast-05641.herokuapp.com/auth/login](https://thawing-coast-05641.herokuapp.com/auth/login).

3. Adding information
Adding information requires account. After logging in, user can see 'Add' item in navigation bar.
   1. Sample
   [https://thawing-coast-05641.herokuapp.com/samples/new/](https://thawing-coast-05641.herokuapp.com/samples/new/)
   Adding sample requires information about the original song and the usage of the sample and time it starts at. Time is added in 'mm:ss' format. If the original song or the song using the sample is not in the database, user can add it by clicking the 'Add song!' link.

   2. Song
   [http://localhost:5000/songs/new/](http://localhost:5000/songs/new/)
   User can add song by giving the songs name and artist. If the artist is not in the database, user can add it by clicking the 'Add missing artist!' link.

   3. Album
   [http://localhost:5000/albums/new/](http://localhost:5000/albums/new/)
   User can add album by giving the albums name, artist and release year. If the artist is not in the database, user can add it by clicking the 'Add missing artist!' link. Release year is limited between 1800 and current year.

   4. Artist
   [http://localhost:5000/artists/new/](http://localhost:5000/artists/new/)
   Adding artist requires only artist name.

4. Lists
Lists are available for everyone. There are 4 different lists(samples, songs, artists, albums) that give summary about the database. Each list contains links to pages containing single item.

5. Single item
Pages for single items in the database.
   1. Sample
    For example page [http://localhost:5000/samples/1/](http://localhost:5000/samples/1/) contains information about single sample. The page tells where the sample is used, what is its origin and what time user can hear the sample in the songs. Page also tells how many times the page has been visited, and who is the owner of the page. If user is logged in as the page owner, deleting the sample becomes available.

    2. Song
    Coming...

