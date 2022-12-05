# Ohjelmistotekniikan harjoitustyö 2022

  
Helsingin Yliopiston Ohjelmistotekniikka-kurssin harjoitustyölle ja laskuharjoituksille tehty repo.

Harjoitustyönä Miinaharava.

*Minesweeper in Python as a school project.*


### Dokumentaatio

[tuntikirjanpito](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[changelog](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[release](https://github.com/Deeroil/ot-harjoitustyo/releases/tag/viikko5)

### Installation and running

First install dependencies by running `poetry install` in the project directory.

Then you can run the app with `poetry run invoke start`


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

Then it will fill a grid with tiles
- 0: empty tiles 
- 1-8: tiles with mines as neighbors
- 9: a tile with a mine

After that, you can give (x,y) coordinates to open tiles of the grid.
After opening a tile, you'll see which number was inside.
If it was 9 (a mine), the game ends.
You can also flag unknown tiles or remove the flag.
You win when you've flagged all tiles with mines.

So the app knows how to
- make a custom sized n*n grid (actually a list)
- fill it with mines (custom amount)
- count how many mines each non-mine tile has as a neighbor (this part is still under construction)
- check a tile and keep track of opened tiles
- mark an unopened tile with a "F" (flag)
- remove a flag
- quit if you hit a mine
- win if you flag all correct tiles
- and a bit more

### Known issues/bugs

- creating a 1x1 grid with 1 mine and trying to open it as the first move (as there are no other options) will cause an infinite loop, as it will try to create a substitute grid where user wouldn't instantly lose, even though this isn't possible

- input will try to convert string to int, this won't work with all inputs and will cause an error

- sometimes the grid will count the neighbors wrong, especially noticeable on 2x2 grids. Not sure yet if this happens only in 2x2 grids.
  - such as

        9  0
        9  2    index 1 should be 2

        1  0
        9  1    index 1 should be 1

        9  9
        1  2    index 2 should be 2