# Changelog

## Viikko 3

- Käyttäjä voi luoda miinaharavaruudukon valinnaisella määrällä ruutuja ja miinoja
  - tässä vielä ongelmia, kesken

## Viikko 4

- Käyttäjä voi avata ruudun pisteestä (x,y) on käyttäen komentoriviä
- Jos avatussa ruudussa on miina (numero 9), peli päättyy
- Kun peli päättyy häviöön, näytetään koko ruudukko pelaajalle ja ohjelma suljetaan
- Ruudukko vaihdetaan jos ensimmäinen avattava ruutu lopettaisi pelin
  - tarkistaa vasta kerran: peli saattaa silti loppua tähän, kesken

## Viikko 5

- käyttäjä voi merkitä avaamattoman ruudun lipulla "F"
- käyttäjä voi poistaa merkitsemänsä lipun
- ruudukon vaihtaminen jos ensimmäinen avattava ruutu lopettaisi pelin toimii nyt vaikka sama tapahtuisi useammin
- käyttäjä voittaa pelin kun kaikki miinat on merkitty lipuilla
- eriytetty tekstikäyttöliittymä omaan luokkaansa ja luokat kansioihin
- lisätty testikattavuutta minesweeper ja grid -luokille
- korjattu miinaruudukon naapurien laskenta