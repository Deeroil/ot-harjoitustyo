from services.grid import Grid


class Minesweeper:
    def __init__(self, grid: Grid):
        self.backgrid = grid
        self.showntiles = []
        for _ in range(grid.width**2):
            self.showntiles.append("_")
        self.mines_total = grid.mines
        self.flags = [] #maybe change to a set?

    # muista selittää että indeksointi alkaa 0:sta ja ylävasemmasta kulmasta TAI muuta näitä
    def check_tile(self, index):
        print(f"chosen tile has number: {self.backgrid.grid[index]}")
        return self.backgrid.grid[index]

    # vois kans olla lista indeksejä jotka on avattu..?
    def add_shown_tiles(self, index):
        number = self.backgrid.grid[index]
        self.showntiles[index] = number
        return number

    def set_flag(self, index):
        flags_left = self.mines_total - len(self.flags)
        print('lippuja:', flags_left)
        if flags_left <= 0:
            print("couldn't set flag! remove one first")
            return
        if self.showntiles[index] != "_" or self.showntiles[index] == "F":
            print("couldn't set flag, as the tile has already been opened or has a flag!")
            return
        self.showntiles[index] = "F"
        self.flags.append(index)

    # TODO: check later
    def remove_flag(self, index):
        if self.showntiles[index] == "_" or self.showntiles[index] != "F":
            print("no flag here!")
            return
        self.flags.remove(index)
        self.showntiles[index] = "_"

    # purkkaa
    def index_has_flag(self, index):
        if index in self.flags:
            return "F"
        else:
          return False

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
            printable += f" {self.index_has_flag(i) or self.showntiles[i]} "
        print(printable)
