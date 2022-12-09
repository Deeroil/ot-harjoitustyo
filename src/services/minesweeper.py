from services.grid import Grid


class Minesweeper:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.showntiles = set()
        self.flags = set()

    # muista selittää että indeksointi alkaa 0:sta ja ylävasemmasta kulmasta TAI muuta näitä
    # tässä on uhkia että otan suoraan indeksin, jos esim antaisi ihan väärät x/y-koordinaatit
    # mutta luku olisi sopiva silti?
    def check_tile(self, index):
        # print(f"chosen tile has number: {self.backgrid.grid[index]}")
        if self.check_index_viability(index) is False:
            return False
        return self.grid.list[index]

    def check_index_viability(self, index):
        if index < 0 or index > self.grid.len:
            print("indeksi ei kelpaa")
            return False
        return True

    # vois kans olla lista indeksejä jotka on avattu..?
    def add_shown_tiles(self, index):
        if self.check_index_viability(index) is False:
            return False

        number = self.grid.list[index]
        self.showntiles.add(index)
        return number

    #checks only by flags
    def check_win(self):
        if len(self.flags) == self.grid.mines:
            for i in self.flags:
                if self.grid.list[i] != 9:
                    return False
            return True
        return False

    def set_flag(self, index):
        if self.check_index_viability(index) is False:
            return
        flags_left = self.grid.mines - len(self.flags)
        # print('lippuja:', flags_left)
        if flags_left <= 0:
            print("lippuja liikaa! poista ensin lippu ")
            return
        if index in self.showntiles or index in self.flags:
            print("ei voitu asettaa lippua, ruutu oli avattu tai siinä oli jo lippu!")
            return
        self.flags.add(index)

    def remove_flag(self, index):
        if self.check_index_viability(index) is False:
            return
        if index not in self.flags:
            print("ei ollut poistettavaa lippua")
            return
        self.flags.remove(index)

    def get_shown_tile(self, index):
        if index in self.flags:
            return "F"
        if index in self.showntiles:
            return self.check_tile(index)
        return "_"

# tulostaa grid jossa näkyy auki klikatut
#     _: avaamaton
#     F: flag, merkitty vaaralliseksi
#   Avatut ruudut:
#     0: tyhjä
#     1-8: ruudulla n naapuria
#     9: pommi/miina
# TODO: rename printables
    def print_current(self):
        bgrid = self.grid
        printable = ""
        for i in range(bgrid.len):
            if i % bgrid.width == 0:
                printable += "\n"
            printable += f" {self.get_shown_tile(i)} "
        print(printable)
