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

[release](https://github.com/Deeroil/ot-harjoitustyo/releases/tag/viikko6)

### Installation and running

First install dependencies by running `poetry install` in the project directory.

Then you can run the app with `poetry run invoke start` to open the desktop version with the graphical user interface.

If you want to run the command-line version of the app instead, run `poetry run invoke command-line`


### Other invoke tasks

`poetry run invoke test` - runs pytest for src

`poetry run invoke coverage` - shows test coverage for src

`poetry run invoke coverage-report` - same as coverage and creates/updates index.html with coverage report

`poetry run invoke lint` - pylint check for src

`poetry run invoke format` - autopep8 formatting for src


### Features

#### Graphical User Interface:

- preset with a 3x3 grid (for now)
- the tiles change border color on hover
- user can open tiles by clicking with left mouse button
  - game ends when a mine is clicked
- user can flag a tile by clicking with right mouse button
- user wins when all of the tiles with a mine have been flagged



#### Command Line Interface:

CLI will ask the user for
- size of the grid (n) and
- how many mines you want there.

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
- count how many mines each non-mine tile has as a neighbor (this part is still under construction)
- check a tile and keep track of opened tiles
- mark an unopened tile with a "F" (flag)
- remove a flag
- quit if you hit a mine
- win if you flag all correct tiles
- and a bit more

### TO-DO
- opening the nearby tiles when opened tile is zero
- set minimum size for grid in CLI app to be 3x3
- and plenty of other stuff, too

### Known issues/bugs

#### in desktop app
- flags flicker and might not be set with a single click
- the GUI could be centered
- little functionality compared to CLI version

#### in command line app
- no errorhandling yet
- most of the code can't handle wrong sort of input
  - for example asking for grid size, mines, coordinates...
  - right now these default to printing stack trace and quitting the program, as expected

- creating a 1x1 grid with 1 mine and trying to open it as the first move (as there are no other options) will cause an infinite loop, as it will try to create a substitute grid where user wouldn't instantly lose, even though this isn't possible
  - should probably set some minimum grid size

- input will try to convert string to int, this won't work with all inputs and will cause an error

- sometimes the grid will count the neighbors wrong, especially noticeable on 2x2 grids. Not sure yet if this happens only in 2x2 grids.
  - such as

        9  0
        9  2    index 1 should be 2

        1  0
        9  1    index 1 should be 1

        9  9
        1  2    index 2 should be 2
  - this isn't an issue as I'll later only allow 3x3 and bigger grids.

- you can open a tile which has a flag, it could have a warning first or just not allow it?