from services.grid import Grid


class Minesweeper:
    """Game functionality for Minesweeper

    Grid is a list for a nxn matrix used in Minesweeper.
    After setting up the grid, the values of the list show which tiles
    have mines and how many mines surround each non-mine tile.

    Args:
        grid: Grid to be used in the game

    Attributes:
        grid: Grid-object with the mines and tiles with neighbor-values related to the mines
        showntiles: A set of all the opened tiles
        flags: A set of tiles flagged by the user

    Example:

    msw = Minesweeper(Grid(3))

    g = Grid(5)

    minesw = Minesweeper(g)
    """
    def __init__(self, grid: Grid):
        self.grid = grid
        self.showntiles = set()
        self.flags = set()

    # muista selittää että indeksointi alkaa 0:sta ja ylävasemmasta kulmasta TAI muuta näitä
    # tässä on uhkia että otan suoraan indeksin, jos esim antaisi ihan väärät x/y-koordinaatit
    # mutta luku olisi sopiva silti?
    def check_tile(self, index):
        # print(f"chosen tile has number: {self.backgrid.grid[index]}")
        if self.grid.check_index_viability(index) is False:
            return False
        return self.grid.list[index]

    # vois kans olla lista indeksejä jotka on avattu..?
    def add_shown_tiles(self, index):
        if self.grid.check_index_viability(index) is False:
            return False

        number = self.grid.list[index]
        self.showntiles.add(index)
        return number

    def check_win(self):
        """Returns true if win condition is fulfilled.

        Checks win condition if amount of flags equals amount of mines in the game.
        If all the flags are set on the mines, game has been won.

        Returns:
            Boolean, True on win and False otherwise.

        """
        if len(self.flags) == self.grid.mines:
            for i in self.flags:
                if self.grid.list[i] != 9:
                    return False
            return True
        return False

    def set_flag(self, index):
        """Removes flag from given list index if the flag exists.

            If the index isn't suitable, nothing happens.
            Prints "lippuja liikaa! poista ensin lippu " if user has set too many
            flags and the flag can't be set.
            Max amount of flags is the total amount of mines.
            Prints "ei voitu asettaa lippua, ruutu oli avattu tai siinä oli jo lippu!"
            if tile in the index has been opened or already has a flag.

            Args:
                index: location of the flag

        """
        if self.grid.check_index_viability(index) is False:
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
        """Removes flag from given list index if the flag exists.

            If the index isn't suitable, nothing happens.
            Prints "ei ollut poistettavaa lippua" if couldn't find flag from that index.

            Args:
                index: location of the flag

        """
        if self.grid.check_index_viability(index) is False:
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

# palauttaa stringinä grid jossa näkyy auki klikatut
#     _: avaamaton
#     F: flag, merkitty vaaralliseksi
#   Avatut ruudut:
#     0: tyhjä
#     1-8: ruudulla n naapuria
#     9: pommi/miina
    def current_state(self):
        """Returns a string showing the current game matrix, from the user's point of view.

            The string will show which tiles have been opened and the value in the
            shown tiles (0-8 for indicating amount of surrounding mines)
            and it shows the flags the user has set.

            Meanings of the symbols:
                0: empty, no neighboring mines
                1-8: indicates the number of mines in surrounding tiles (neighbors)
                9: a mine

            Returns:
                String presenting the grid's shown tiles to the user.

        """
        bgrid = self.grid
        printable = ""
        for i in range(bgrid.len):
            if i % bgrid.width == 0:
                printable += "\n"
            printable += f" {self.get_shown_tile(i)} "
        return printable
