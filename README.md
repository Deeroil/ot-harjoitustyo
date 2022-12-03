# Ohjelmistotekniikan harjoitustyö 2022

  
Helsingin Yliopiston Ohjelmistotekniikka-kurssin harjoitustyölle ja laskuharjoituksille tehty repo.

Harjoitustyönä Miinaharava.

*Minesweeper in Python as a school project.*


### Dokumentaatio

[tuntikirjanpito](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[changelog](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

### Installation and running

Install dependencies by running `poetry install`

Run the app with `poetry run invoke start`


### Other invoke tasks

`poetry run invoke test` - runs pytest for src

`poetry run invoke coverage` - shows test coverage for src

`poetry run invoke coverage-report` - same as coverage and creates/updates index.html with coverage report

`poetry run invoke lint` - pylint check for src

`poetry run invoke format` - autopep8 formatting for src


### Features
The command line interface is very simple right now
It will ask you for
- size of the grid (n) and
- how many mines you want there.

Then it will print a grid with tiles
- 0: empty tiles 
- 1-8: tiles with mines as neighbors
- 9: a tile with a mine

After that, you can give (x,y) coordinates to open tiles of the grid.
After opening a tile, you'll see which number was inside.
If it was 9 (a mine), the game ends.

You can't win yet, and you can only quit by hitting a mine or otherwise quitting the program.


So the app knows how to
- make a custom sized n*n grid (actually a list)
- fill it with mines (custom amount)
- count how many mines each non-mine tile has as a neighbor (this part is still under construction)
- check a tile and keep track of opened tiles
- mark an unopened tile with a "F" (flag)
- remove a flag
- quit if you hit a mine
- and a bit more