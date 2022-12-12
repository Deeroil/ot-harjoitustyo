# Miinaharava CLI käyttöohje

>> EDIT THESE Aloita lataamalla projektin  [releasen](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

Graafisen käyttöliittymän sisältämän version käyttöohje [täällä](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

## Asentaminen ja käynnistäminen

Ensin asenna riippuvuudet komennolla:

```
poetry install
```

Tämän jälkeen komentoversio ohjelmasta käynnistetään komennolla 

```
poetry run invoke commmand-line
```

Ohjelma käynnistyy komentoriviltä.

## Miinaharava

### Tavoite

Pelin tavoitteena on selviytyä miinakentästä avaamalla ruutuja, jotta voi päätellä ja merkitä lipulla ruudut joissa on miina. Peli päättyy heti jos osutaan miinaan. Jos ruudussa ei ole miinaa, näkyy ruudussa numero, joka kertoo kuinka monta miinaa on kyseistä ruutua ympäröivissä ruuduissa yhteensä. Peli voitetaan merkitsemällä kaikki miinat lipuilla.

### Peliruudukon alustus
Ohjelma alkaa kysymällä halutun ruudukon kokoa. Tässä koko viittaa nxn-kokoisen ruudukon sivun pituuteen, esim luvulla 3 tulee seuraavan kokoinen ruudukko:

```
0 0 0
0 0 0
0 0 0
```

Luvulla 0 tai alle, ohjelma sulkeutuu.

Seuravaaksi ohjelma pyytää miinojen määrää. Miinojen määrän ollessa 0 tai alle, tai jos miinoja olisi useampi kuin ruudukossa paikkoja, ohjelma sulkeutuu.

Tämän jälkeen alkuvalmistelut on tehty, ja peli alkaa. (Tällä hetkellä peli myös tulostaa ruudukon eli vastaukset.)

### Pelin toiminta

Käyttäjä voi avata ruudun antamalla x- ja y-koordinaatteja komentorivillä.

Koordinaatit alkavat numerosta 0, vasemmasta ylänurkasta. Esimerkki koordinaateista 3x3-ruudukkoon, koordinaatit merkitty (x, y):

```
(0,0)   (1,0)   (2,0)
(0,1)   (1, 1)  (2, 1)
(0,2)   (1, 2)  (2, 2)

```

Tällöin ruudun alta paljastuu joko miina, jolloin peli päättyy häviöön, tai numero, joka merkitsee viereisissä ruuduissa olevien miinojen määrää.

Pelaajalta kysytään ensimmäisen avatun ruudun jälkeen myös, haluaako hän merkitä jonkun ruuduista lipulla, tai poistaa lipun jostain ruudusta.
Tällöin vastataan kirjoittamalla komentoriville F (flag, halutaan asettaa ruutuun lippu) tai R (remove, halutaan poistaa ruudusta lippu). Lippu kuvastaa ruutua, jonka alla pelaaja uskoo olevan miina. Lippuja voi asettaa yhteensä yhtä monta kuin miinoja on ruudukossa.

Peli voitetaan jos kaikki miinat saadaan merkittyä oikein lipuilla ilman että osutaan miinaan.

Peli hävitään jos pelaaja avaa ruudun, jossa oli miina. Tällöin ohjelma tulostaa ruudukon jossa näkyy kaikki miinat ja niiden naapurit, ja ohjelma sulkeutuu.



