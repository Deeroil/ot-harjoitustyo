# Vaatimusmäärittely

## Sovelluksen tarkoitus
Miinaharava-pelin pelaaminen työpöytäsovelluksena

## Perusversion tarjoama toiminnallisuus

### Pelinäkymä
* Käyttäjä voi "avata" peliruudukosta kerralla yhden ruudun
	* Jos ruudussa on miina, peli päättyy
		* ensimmäisellä kierroksella ensimmäinen klikkaus ei voi osua miinaan
		* Kun peli päättyy näin, näytetään kaikkien miinojen sijainnit
	* Sen sijaan jos ruudulla on naapurina miina/miinoja, tulee näkyviin kyseinen numero
	* Jos ruutu on "tyhjä" eli ruudussa ei ole miinaa eikä sen välittömänä naapurina ole miinaa/miinoja, paljastuu ruudukosta alue joka on reunustettu naapurinumeroita sisältävillä ruuduilla.
		* Jos tyhjiä ruutuja on useampi lähekkäin, avautuu suurempi alue
* Käyttäjä voi merkitä peliruudukon ruudun "vaaralliseksi". Vaarallisuus merkitsee miinan oletettua sijaitsemiskohtaa. Vaaralliseksi voi merkitä vain yhtä monta ruutua kuin miinoja on peliruudukossa.
* Peli voitetaan kun käyttäjä on merkannut kaikki miinat vaarallisiksi osumatta yhteenkään miinaan.
* Pelin päättyessä voi aloittaa pelin alusta

## Jatkokehitysideoita
Perusversion toteuttamisen jälkeen voidaan kehittää mm. seuraavin tavoin:
* Käyttäjä voi käyttää sekä näppäimistöä että hiirtä toimintoihin
### Ennen peliä ja asetukset
- Käyttäjä voi valita peliruudukon koon useammasta valmiiksi määritellystä vaihtoehdosta
	- Peliruudukon koon valitseminen omavalintaisesti rajatulta väliltä
- Käyttäjä voi valita miinojen määrän useammasta valmiiksi määritellystä vaihtoehdosta
	- Miinojen määrän valitseminen kustomoidusti rajatulta väliltä
- Pelin haastavuuden lisääminen, erilaiset pelimuodot
### UI
- Graafinen käyttöliittymä
- Peliruudukon ja/tai käyttöliittymän värien kustomointi itse valittujen värien mukaan
	- näiden asetusten tallentaminen
- Animaatioita ja niille toggle-mahdollisuus (on/off)
- Kustomoitavat teemat joista valita

### Pelissä
- Pelin voi aloittaa alusta kesken pelin
- Käyttäjä näkee jäljellä olevan miinojen oletetun lukumäärän, vaarallisiksi merkattujen ruutujen määrän perusteella
- Käyttäjä voi merkata avaamattoman ruudun kysymysmerkillä
- Pelin keston laskeminen sekunneissa
- Pelaaminen ajastetusti, käyttäjä häviää jos ei ole tarpeeksi nopea
- Mahdollisuus pelitilan tallentamiseen mm. kun peli suljetaan

### Pelin jälkeen
- High score -näyttö ja sen tietojen tallettaminen tietokantaan
- High scoreen uniikin nimimerkin valitseminen
	- salasanalukitsemisen mahdollisuus nimimerkille
