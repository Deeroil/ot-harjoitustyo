# Vaatimusmäärittely

## Sovelluksen tarkoitus
Miinaharava-pelin pelaaminen työpöytäsovelluksena

## Perusversion tarjoama toiminnallisuus

### Graafinen käyttöliittymä

### Pelinäkymä
* Käyttäjä voi klikata peliruudukosta auki ruudun hiiren vasemmalla näppäimellä
	* jos ruudussa on miina, hävitään peli ja ohjelma sulkeutuu
	* jos ruudussa ei ollut miinaa, ruudussa lukee viereisten miinojen määrä
	* Jos ruutu on "tyhjä" eli ruudussa ei ole miinaa eikä sen välittömänä naapurina ole miinaa/miinoja, paljastuu ruudukosta alue joka on reunustettu naapurinumeroita sisältävillä ruuduilla.
* Käyttäjä voi merkata avaamattomaan ruutuun lipun hiiren oikealla näppäimellä. Uudestaan klikkaaminen poistaa lipun.
* Käyttäjä voi laittaa lipun vain yhtä moneen ruutuun kuin miinoja on peliruudukossa.
* Peli voitetaan merkitsemällä oikeat ruudut lipulla, tästä näkyy ilmoitus käyttäjälle
* Peli myös voitetaan jos käyttäjä on avannut kaikki ruudut paitsi ne joissa on miina

- Pelin voi aloittaa alusta kesken pelin
- Pelitila tallennetaan kun peli suljetaan, ja peli jatkuu samasta kohdasta kun peli avataan uudestaan.
- Käyttäjä näkee pelin kaikkien miinojen lukumäärän
- Käyttäjä jäljellä olevien lippujen lukumäärän
- Käyttäjä näkee montako voittoa on saanut putkeen
- Käyttäjän paras voittoputki tallennetaan tietokantaan
- Kolme parasta voittoputkea näytetään käyttäjälle


### Komentoriviversio

### Ennen peliä
- Käyttäjä voi valita peliruudukon koon useammasta valmiiksi määritellystä vaihtoehdosta
	- Peliruudukon koon valitseminen omavalintaisesti, rajatulta väliltä
 	- Miinojen määrän valitseminen kustomoidusti rajatulta väliltä

### Pelinäkymä

* Käyttäjä voi "avata" peliruudukosta kerralla yhden ruudun
	* Jos ruudussa on miina, peli päättyy
	* ensimmäisellä kierroksella ensimmäinen avattu ruutu ei voi osua miinaan
	* Jos klikatulla ruudulla on naapurina miina/miinoja, tulee näkyviin kyseinen numero
	* Jos ruutu on "tyhjä" eli ruudussa ei ole miinaa eikä sen välittömänä naapurina ole miinaa/miinoja, paljastuu ruudukosta alue joka on reunustettu naapurinumeroita sisältävillä ruuduilla.
	* Jos ruutu on tyhjä ja tyhjiä ruutuja on useampi lähekkäin, avautuu suurempi alue
	* Käyttäjä voi merkitä peliruudukon ruudun "vaaralliseksi" lipulla. Lippu kuvaa miinan oletettua sijaitsemiskohtaa. Lipun voi myös poistaa.
	* Lipulla voi merkitä vain yhtä monta ruutua kuin miinoja on peliruudukossa.
	* Kun peli päättyy miinaan, näytetään kaikkien miinojen sijainnit
		* näyttää koko taustaruudukon
* Peli voitetaan kun käyttäjä on merkannut kaikki miinat lipuilla osumatta yhteenkään miinaan
* Peli myös voitetaan jos käyttäjä on avannut kaikki ruudut paitsi ne joissa on miina
* Käyttäjä voi aloittaa uuden pelin voittaessaan sulkematta ohjelmaa

## Jatkokehitysideoita
Perusversion toteuttamisen jälkeen voidaan kehittää mm. seuraavin tavoin:

### Asetukset
- Käyttäjä voi valita graafisessa käyttöliittymässä peliruudukon koon ja miinojen määrän useammasta valmiiksi määritellystä vaihtoehdosta
- Pelin haastavuuden lisääminen, erilaiset pelimuodot

### UI
- Käyttäjän nimen vaihtaminen, mm. voittoputki-highscoreja varten
- Peliruudukon ja/tai käyttöliittymän värien kustomointi itse valittujen värien mukaan
	- näiden asetusten tallentaminen
- Animaatioita ja niille toggle-mahdollisuus (on/off)
- Kustomoitavat teemat joista valita
- Kuva kirjaimen "F" tilalle tarkoittamaan lippua

### Pelissä
- Lipun voi asettaa vain jos lipun vieressä on jokin avattu ruutu
- Käyttäjä voi merkata avaamattoman ruudun kysymysmerkillä
- Pelin keston laskeminen sekunneissa
- Pelaaminen ajastetusti, käyttäjä häviää jos ei ole tarpeeksi nopea
- Käyttäjä voi käyttää sekä näppäimistöä että hiirtä toimintoihin

### muut
- Tietokannan kehittäminen
	- tallennetaan vain parhaat 4 tulosta per käyttäjä
	- mahdollisuus asettaa salasana käyttäjälle
	- myös muiden tietojen tallentaminen, kuten nopeus
	- eri highscoret eri kokoisille ruudukoille