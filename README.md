# Whosampledthis

For database application course in 2019.

Whosampledthis is an application for finding information about [audio samples](https://en.wikipedia.org/wiki/Sampling_(music)) used in songs.

[App on heroku](https://thawing-coast-05641.herokuapp.com/)

Test credentials:

username: tes
password: ti

## Documentation

[Database diagram](documentation/database_diagram.png)
[User stories](documentation/user_stories.md)

## Kuvaus

Whosampledthis on palvelu johon käyttäjät voivat syöttää kappaleita, tietoja niiden käyttämistä sampleista ja tietoja siitä missä kyseisestä kappaleesta tehtyjä sampleja on käytetty.

Kuka tahansa voi tutkia tietoja kappaleista, sampleista sekä kappaleiden ja samplejen relaatioista. Kirjautuneet käyttäjät voivat lisätä kappaleita palveluun ja merkitä, jos kappale on käyttänyt sampleja jostain jo palvelussa olevasta kappaleesta tai vielä palvelussa olemattomasta kappaleesta. Jälkimmäisessä tapauksessa käyttäjältä kysytään myös toisen kappaleen tietoja. Kirjautuneet käyttäjät voivat myös muokata jo olemassa olevien kappaleiden tietoja.

Kappaleista lisättäviin tietoihin kuuluvat kappaleen nimi, albumi, tekijä ja julkaisuvuosi. Sampletiedon lisäämisen yhteydessä linkitetään kaksi kappaletta toisiinsa ja kerrotaan molemmista kappaleista missä kohtaa kappaletta samplattu kohta esiintyy.

Toimintoja:
- Kirjautuminen
- Kappaleen syöttö ja muokkaus
- Kappaleiden etsiminen ja katselu (kappaleen, albumin ja artistin perusteella)
- Kappaleen samplejen listaus ja linkit alkuperäisiin kappaleisiin
- Suosituimpien samplejen listaus (katseluiden perusteella)
- Viimeisimmät lisäykset
- Admin käyttäjät voivat hallinnoida kirjautuneita käyttäjiä sekä lisätä, muokata ja poistaa kappaleita.
