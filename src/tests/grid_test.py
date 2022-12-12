import unittest
from services.grid import Grid

# TODO:
# test grid_list with negatives and 0, 1.
# test neighbors, bounds, etc
# test error handling later? can't make more mines than there are tiles etc


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(5)
        self.grid2 = Grid(3)
        self.grid2x2 = Grid(2)

    def test_grid_length_matches_5x5_grid(self):
        self.assertEqual(len(self.grid.list), 25)

    def test_grid_len_matches_5x5_grid(self):
        self.assertEqual(self.grid.len, 25)

    def test_set_mines_adds_one_mine(self):
        self.grid.set_mines(1)
        mines = 0
        for i in self.grid.list:
            if i == 9:
                mines += 1
        self.assertEqual(mines, 1)

    def test_set_mines_adds_6_mines(self):
        self.grid.set_mines(6)
        mines = 0
        for i in self.grid.list:
            if i == 9:
                mines += 1
        self.assertEqual(mines, 6)

    def test_set_mines_wont_add_too_many_mines(self):
        self.grid.set_mines(30)
        mines = 0
        for i in self.grid.list:
            if i == 9:
                mines += 1
        self.assertEqual(mines, 0)

    #check index viability
    def test_check_index_viability_with_0_returns_True(self):
        self.assertTrue(self.grid.check_index_viability(0))

    def test_check_index_viability_with_last_index_returns_True(self):
        self.assertTrue(self.grid.check_index_viability(self.grid.len - 1))
    
    def test_check_index_viability_with_length_returns_False(self):
        self.assertFalse(self.grid.check_index_viability(self.grid.len))

    def test_check_index_viability_with_neg_one_returns_False(self):
        self.assertFalse(self.grid.check_index_viability(-1))
    
    def test_check_index_viability_with_too_big_index_returns_False(self):
        self.assertFalse(self.grid.check_index_viability(100))

    def test_check_index_viability_with_ok_index_returns_True(self):
        self.assertTrue(self.grid.check_index_viability(4))

    #set neighbors
    def test_set_neighbors_with3x3_and_one_mine(self):
        compare_grid = [1,1,1,1,9,1,1,1,1]
        self.grid2.list[4] = 9 #setting a mine
        self.grid2.set_neighbors()
        self.assertEqual(self.grid2.list, compare_grid)

    def test_set_neighbors_5x5_2mines_1(self):
        compare_grid = [1,1,1,0,0,
                        1,9,1,0,0,
                        1,1,1,0,0,
                        0,0,0,1,1,
                        0,0,0,1,9]
        self.grid.list[6] = 9
        self.grid.list[24] = 9
        self.grid.set_neighbors()
        self.assertEqual(self.grid.list, compare_grid)

    def test_set_neighbors_3x3_3mines_1(self):
        compare_grid = [2,9,2,
                        3,9,3,
                        2,9,2]
        self.grid2.list[1] = 9
        self.grid2.list[4] = 9
        self.grid2.list[7] = 9
        self.grid2.set_neighbors()
        self.assertEqual(self.grid2.list, compare_grid)

    def test_set_neighbors_3x3_corners(self):
        compare_grid = [9,2,9,
                        2,4,2,
                        9,2,9]
        self.grid2.list[0] = 9
        self.grid2.list[2] = 9
        self.grid2.list[6] = 9
        self.grid2.list[8] = 9
        self.grid2.set_neighbors()
        self.assertEqual(self.grid2.list, compare_grid)

    def test_str(self):
        compare_str = "\n 0  1  2 \n 3  4  5 \n 6  7  8 "
        self.grid2.list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(str(self.grid2), compare_str)