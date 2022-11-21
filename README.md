# Ohjelmistotekniikan harjoitustyö 2022

  
Helsingin Yliopiston Ohjelmistotekniikka-kurssin harjoitustyölle ja laskuharjoituksille tehty repo.

Harjoitustyönä Miinaharava.

*Minesweeper in Python as a school project.*


### Dokumentaatio

[tuntikirjanpito](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaatimusmäärittely](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[changelog](https://github.com/Deeroil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)


### Installation and running

Install dependencies by running `poetry install`

Run the app with `poetry run invoke start`


### Features
The command line interface is very simple right now
It will ask you for
- size of the grid (n) and
- how many mines you want there.

Then it will print a grid with tiles
- 0: empty tiles 
- 1-8: tiles with mines as neighbors
- 9: a tile with a mine

So there isn't any game functionality yet.

So the app knows just how to
- make a custom sized n*n grid (actually a list)
- fill it with mines
- count how many mines each non-mine tile has as a neighbor (this part is still under construction, well most of this is.)