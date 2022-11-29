from grid import Grid

# TODO: onks mitkä näistä käli-asioita? uh oh


class Minesweeper:
    def __init__(self, grid: Grid):
        self.backgrid = grid
        self.showntiles = []
        for _ in range(grid.width**2):
            self.showntiles.append("_")

    # muista selittää että indeksointi alkaa 0:sta ja ylävasemmasta kulmasta TAI muuta näitä
    def check_tile(self, index):
        print(f"chosen tile has number: {self.backgrid.grid[index]}")
        return self.backgrid.grid[index]

    # vois kans olla lista indeksejä jotka on avattu..?
    def add_shown_tiles(self, index):
        number = self.backgrid.grid[index]
        self.showntiles[index] = number
        return number

# tulostaa grid jossa näkyy auki klikatut
#     _: avaamaton
#     F: flag, merkitty vaaralliseksi
#   Avatut ruudut:
#     0: tyhjä
#     1-8: ruudulla n naapuria
#     9: pommi/miina
# TODO: rename printables
    def print_current(self):
        bgrid = self.backgrid
        printable = ""
        for i in range(bgrid.len):
            if i % bgrid.width == 0:
                printable += "\n"
            printable += f" {self.showntiles[i]} "
        print(printable)
