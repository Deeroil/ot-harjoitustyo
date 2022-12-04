from services.grid import Grid


class Minesweeper:
    def __init__(self, grid: Grid):
        self.backgrid = grid
        self.showntiles = []
        for _ in range(grid.width**2):
            self.showntiles.append("_")
        self.mines_total = grid.mines
        self.flags = set()

    # muista selittää että indeksointi alkaa 0:sta ja ylävasemmasta kulmasta TAI muuta näitä
    # tässä on uhkia että otan suoraan indeksin, jos esim antaisi ihan väärät x/y-koordinaatit
    # mutta luku olisi sopiva silti?
    def check_tile(self, index):
        # print(f"chosen tile has number: {self.backgrid.grid[index]}")
        if self.check_index_viability(index) is False:
            return False
        return self.backgrid.grid[index]

    def check_index_viability(self, index):
        if index < 0 or index > self.backgrid.len:
            print("index not viable")
            return False
        return True

    # vois kans olla lista indeksejä jotka on avattu..?
    def add_shown_tiles(self, index):
        if self.check_index_viability(index) is False:
            return False
        number = self.backgrid.grid[index]
        self.showntiles[index] = number
        return number

    #checks only by flags
    def check_win(self):
        if len(self.flags) == self.mines_total:
            for i in self.flags:
                if self.backgrid.grid[i] != 9:
                    return False
            return True
        return False

    def set_flag(self, index):
        if self.check_index_viability(index) is False:
            return
        flags_left = self.mines_total - len(self.flags)
        print('lippuja:', flags_left)
        if flags_left <= 0:
            print("couldn't set flag! remove one first")
            return
        if self.showntiles[index] != "_" or self.showntiles[index] == "F":
            print("couldn't set flag, as the tile has already been opened or has a flag!")
            return
        self.showntiles[index] = "F"
        self.flags.add(index)

    # ehkä helpompi vaan tehdä index_has_flag avulla?
    def remove_flag(self, index):
        if self.check_index_viability(index) is False:
            return
        if self.showntiles[index] == "_" or self.showntiles[index] != "F":
            print("no flag here!")
            return
        self.flags.remove(index)
        self.showntiles[index] = "_"

    def index_has_flag(self, index):
        if index in self.flags:
            return "F"
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
