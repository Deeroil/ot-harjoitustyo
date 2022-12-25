# Ohjelmistotekniikan harjoitustyö 2022

  
Helsingin Yliopiston Ohjelmistotekniikka-kurssin harjoitustyölle ja laskuharjoituksille tehty repo.

Harjoitustyönä Miinaharava.

Miinaharava on logiikkapeli, jossa yritetään päätellä ruudukon kaikki ruudut joissa ei ole miinaa. Pelin alkutilanteessa on ruudukko avaamattomia ruutuja, joista joidenkin taakse on piilotettu miina. Miinojen lukumäärä pelin aloittaessa tiedetään. Ruutuja avaamalla pelaaja saa tietää, onko kyseisessä ruudussa miina. Jos miina löytyy, peli päättyy. Jos ruudussa ei ole miinaa, ilmestyy avatun ruudun kohdalle numero joka kertoo kuinka moni kyseisen ruudun vierekkäisistä ruuduista sisältää miinan.

*Minesweeper in Python as a school project.*


### Dokumentaatio / Documentation, in Finnish

[tuntikirjanpito](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[käyttöohje (gui)](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[käyttöohje (cli)](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje_cli.md)

[changelog](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[testausdokumentti](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[release](https://github.com/Deeroil/ot-harjoitustyo/releases/tag/viikko6)

### Installation and running

First install dependencies by running `poetry install` in the project directory.

If this is your first time running the program, initialize database with `poetry run invoke build` before starting the game. (you can skip this step if you will only use the command-line program)

Then you can run the app with `poetry run invoke start` to open the desktop version with the graphical user interface.

If you want to run the command-line version of the app instead, run `poetry run invoke command-line`

If "command invoke is not found" or that sort of error occurs, try to `poetry install` again.


### Other invoke tasks

`poetry run invoke test` - runs pytest for src

`poetry run invoke coverage` - shows test coverage for src

`poetry run invoke coverage-report` - same as coverage and creates/updates index.html with coverage report

`poetry run invoke lint` - pylint check for src

`poetry run invoke format` - autopep8 formatting for src


### Features

#### Graphical User Interface:

- preset with a 10x10 grid
- the tiles change border color on hover
- user can open tiles by clicking with left mouse button
  - if the tile is empty, neighboring tiles are shown
  - if empty tile has neighboring empty tiles, they're opened
  - game ends when a mine is clicked
- user can flag a tile by clicking with right mouse button
- user wins when all of the tiles with a mine have been flagged, or all non-mine tiles have been opened
- sidebar with buttons
- saves file on quit
- keeps track of top three win streaks



#### Command Line Interface:

CLI will ask the user for
- size of the grid (n) and
- how many mines to plant.

Then it will fill a grid with tiles
- 0: empty tiles 
- 1-8: tiles with mines as neighbors
- 9: a tile with a mine (will probably change this to some other sign later)

After that, you can give (x,y) coordinates to open tiles of the grid.
After opening a tile, you'll see which number was inside.
If it was 9 (a mine), the game ends.
You can also flag unknown tiles or remove the flag.
You win when you've flagged all tiles with mines.

So the cli program knows how to
- make a custom sized n*n grid (actually a list)
- fill it with mines (custom amount)
- count how many mines each non-mine tile has as a neighbor
- check a tile and keep track of opened tiles
- open neighbors of an empty tile when its clicked
- open neighboring empty tiles of an empty, clicked mine
- mark an unopened tile with a "F" (flag)
- remove a flag
- quit if you hit a mine
- win if you flag all correct tiles
- and a bit more