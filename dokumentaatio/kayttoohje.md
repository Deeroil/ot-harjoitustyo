# Miinaharava GUI käyttöohje

Aloita lataamalla projektin viimeisimmän [releasen](https://github.com/Deeroil/ot-harjoitustyo/releases) lähdekoodi lataamalla _Assets_-osion alta _Source code_.

Linkki komentorivikäyttöliittymän käyttöohjeeseen [tässä](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje_cli.md)

## Asentaminen ja käynnistäminen

Ensin asenna riippuvuudet komennolla:

```
poetry install
```

Tämän jälkeen GUI-versio ohjelmasta käynnistetään komennolla 

```
poetry run invoke start
```

Aukeaa uusi ikkuna, jossa on peliruudukko ja peli voi alkaa.

## Miinaharava

### Tavoite

Pelin tavoitteena on selviytyä miinakentästä avaamalla ruutuja, jotta voi päätellä ja merkitä lipulla ruudut joissa on miina. Peli päättyy heti jos osutaan miinaan. Jos ruudussa ei ole miinaa, näkyy ruudussa numero, joka kertoo kuinka monta miinaa on kyseistä ruutua ympäröivissä ruuduissa yhteensä. Peli voitetaan merkitsemällä kaikki miinat lipuilla.

### Pelin toiminta

Tällä hetkellä ohjelma aukeaa suoraan näyttäen 3x3-kokoisen peliruudukon, jossa on piilossa 3 miinaa. Muun kokoisia ruudukoita ei ole vielä mahdollista valita.

Käyttäjä voi avata ruudun klikkaamalla hiiren vasenta painiketta ruudun päällä. Kun hiiri on ruudun päällä, sen reunat ovat eri väriset. Klikatessa ruutua sen alta paljastuu joko miina, jolloin peli päättyy häviöön, tai numero, joka merkitsee viereisissä ruuduissa olevien miinojen määrää.

Avaamattoman ruudun voi merkitä lipulla painaen hiiren oikealla painikkeella. Lippu (F) kuvastaa ruutua, jonka alla pelaaja uskoo olevan miina.
Samalla tavalla uudestaan klikkaamalla voi poistaa lipun ruudusta. Lippuja voi asettaa yhteensä yhtä monta kuin miinoja on ruudukossa.

Peli voitetaan jos kaikki miinat saadaan merkittyä oikein lipuilla ilman että osutaan miinaan.

Peli hävitään jos pelaaja avaa ruudun, jossa oli miina. Tällöin ohjelma sulkeutuu hetken kuluttua.



