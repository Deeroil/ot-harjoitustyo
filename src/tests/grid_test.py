import unittest
from grid import Grid

# TODO:
# test grid_list with negatives and 0, 1.
# test neighbors, bounds, etc
# test error handling later? can't make more mines than there are tiles etc


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(5)
        self.grid2 = Grid(3)

    def test_grid_length_matches_5x5_grid(self):
        self.assertEqual(len(self.grid.grid), 25)

    def test_grid_len_matches_5x5_grid(self):
        self.assertEqual(self.grid.len, 25)

    def test_set_mines_adds_one_mine(self):
        self.grid.set_mines(1)
        mines = 0
        for i in self.grid.grid:
            if i == 9:
                mines += 1
        self.assertEqual(mines, 1)

    def test_set_mines_adds_6_mines(self):
        self.grid.set_mines(6)
        mines = 0
        for i in self.grid.grid:
            if i == 9:
                mines += 1
        self.assertEqual(mines, 6)

    def test_set_mines_wont_add_too_many_mines(self):
        self.grid.set_mines(30)
        mines = 0
        for i in self.grid.grid:
            if i == 9:
                mines += 1
        self.assertEqual(mines, 0)

    # def test_set_neighbors_with_1_mine(self):
    # grid like 000 090 000  sets 111 191 111?

    #remember to also test that the functionality works as intended!
    def test_set_neighbors_with3x3_and_one_mine(self):
        compare_grid = [1,1,1,1,9,1,1,1,1]
        self.grid2.grid[4] = 9 #setting a mine
        self.grid2.set_neighbors()
        self.assertEqual(self.grid2.grid, compare_grid)