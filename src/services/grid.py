from random import shuffle


class Grid:
    """Class for setting up a grid for minesweeper.

    Grid is a list for a nxn matrix used in Minesweeper.
    After setting up the grid, the values of the list show which tiles
    have mines and how many mines surround each non-mine tile.

    Args:
        width: width of the grid

    Attributes:
        list: all of the tiles on the grid
        width: amount of rows (or columns) the grid has
        len: size of the list
        mines: total amount of mines (number 9) in the list

    Example for making an empty 3x3 grid

    grid = Grid(3)
    """
    def __init__(self, width):
        """Constructor for creating empty nxn-sized grid. The grid is operated as a list.

        Args:
            width: An integer indicating the amount of rows (or columns) the grid has

        """
        self.list = []
        self.width = width
        self.len = width**2
        for _ in range(width**2):
            self.list.append(0)
        self.mines = 0

    def set_mines(self, amount):
        """Sets given amount of mines on the list and randomizes the order.

            The amount of mines can't be more than indices in the list.

            Args:
                amount: Number of the mines.

        """
        if len(self.list) < amount or amount < 0:
            print('errorhandling here')
            return
        self.mines = amount

        for i in range(0, amount):
            self.list[i] = 9  # 9 = a mine

        shuffle(self.list)

    def check_index_viability(self, index):
        """Checks if index is within the bounds of the grid's list.

            Also prints out "indeksi ei kelpaa" if the index isn't suitable.

            Args:
                index: Integer, an index of the list to be checked

            Returns:
                True if index is within range, otherwise False.

        """

        if index < 0 or index >= self.len:
            print("indeksi ei kelpaa")
            return False
        return True

    # TODO: rename to neighbors
    def check_neighbors(self, index):
        """Returns all valid neighbor indices for an index.

            Checks all possible indices for given index and adds them to a set.
            Then checks which indices are out of bounds, as the matrix/grid is presented as a list.
            Doesn't work on 1x1 or 2x2 grids.

            Args:
                index: Integer, an index of the list to be checked.

            Returns:
                A set with all of the valid neighbor indices for that index.

                False if index viability check doesn't pass.

        """
        if self.check_index_viability(index) is False:
            return False

        top_row = {index - self.width - 1, index - self.width, index - self.width + 1}
        bottom_row = {index + self.width - 1, index + self.width, index + self.width + 1}
        left_col = {index - self.width - 1, index - 1, index + self.width - 1}
        right_col = {index - self.width + 1, index + 1, index + self.width + 1}

        neighbor_indexes = top_row | bottom_row | left_col | right_col

        if 0 <= index <= self.width - 1: #index on top row
            neighbor_indexes -= top_row

        if self.len - self.width <= index <= self.len - 1: #index on bottom row
            neighbor_indexes -= bottom_row

        if index % self.width == 0: #index on left column
            neighbor_indexes -= left_col

        if index % self.width == self.width - 1: #index on right column
            neighbor_indexes -= right_col

        return neighbor_indexes

    def count_neighbors(self, index):
        """Counts how many mines a tile/index has as neighboring tiles.

            Args:
                index: Integer, an index of the list to be checked

            Returns:
                Number of mines as an integer.
                False if index viability check doesn't pass.

        """

        if self.check_index_viability(index) is False:
            return False

        neighbor_indexes = self.check_neighbors(index)

        mines = 0
        for i in neighbor_indexes:
            if i < 0 or i >= self.len:
                continue
            if self.list[i] == 9:
                mines += 1
        return mines

    def set_neighbors(self):
        """Sets the number of neighbors of a tile, for every non-mine tile.

            Changes list content to express the amount of mines
            each non-mine tile has as a neighbor.
            If index n has 4 mines surrounding it as its neighbors,
            number 4 will be stored in list[n].
        """
        for i in range(self.len):
            if self.list[i] == 9:
                continue
            self.list[i] = self.count_neighbors(i)

    def __str__(self):
        """Returns a string showing the list as a nxn sized matrix.

            The string will show all of the locations of the mines
            and how many neighboring mines each tile has.

            Meanings of the symbols:
                0: empty, no neighboring mines
                1-8: indicates the number of mines in surrounding tiles (neighbors)
                9: a mine

            Returns:
                String presenting the neighbor/mine values of the grid.

        """
        printable = ""
        for i in range(self.len):
            if i % self.width == 0:
                printable += "\n"
            printable += f" {self.list[i]} "
        return printable
