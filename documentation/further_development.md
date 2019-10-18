# Further development

## Next steps
- Add possibility to add more than one artist to a song
- Song's artists changeable
- When adding song use automatically album's artist as song's artist
- More power to admin. Edit and remove all things, including albums, artists and users.
- Pagination to SQL queries
- Change local development database to PostgreSQL
- Get rid of 'hackish' queries, for example getting album with most samples uses ordering when it really should use max and get only one item as a result



## More
- Removing Song-Artist relationship and adding Song-Featuring_Artist relation would be closer to real life, but I am not really so sure if it would make the database better