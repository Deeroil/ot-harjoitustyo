import unittest
from services.grid import Grid
from services.minesweeper import Minesweeper


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.test_grid = Grid(3)
        self.test_grid.list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.minesw = Minesweeper(self.test_grid)

    def test_check_tile_1_2(self):
        self.assertEqual(self.minesw.check_tile(7), 7)

    def test_check_tile_0_0(self):
        self.assertEqual(self.minesw.check_tile(0), 0)

    def test_check_tile_false(self):
        self.assertFalse(self.minesw.check_tile(0), 10)

    def test_shown_tiles_index_2_is_underscore(self):
        self.assertEqual(self.minesw.showntiles[2], "_")

    def test_add_shown_tiles_adds_to_shown(self):
        self.minesw.add_shown_tiles(3)
        self.assertEqual(self.minesw.showntiles[3], 3)

    #Flag tests

    def test_set_flag_works_on_unopened_tile_when_grid_has_mines(self):
        self.minesw.grid.mines = 2
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.showntiles[1], "F")
        self.assertIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 1)

    def test_set_flag_doesnt_set_if_no_mines(self):
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.showntiles[1], "_")
        self.assertNotIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 0)   

    def test_set_flag_doesnt_set_if_not_enough_mines_left(self):
        self.minesw.grid.mines = 1
        self.minesw.set_flag(1)
        self.minesw.set_flag(2)
        self.assertEqual(self.minesw.showntiles[2], "_")
        self.assertNotIn(2, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 1)

    def test_set_flag_doesnt_change_anything_if_flag_exists(self):
        self.minesw.grid.mines = 2
        self.minesw.set_flag(1)
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.showntiles[1], "F")
        self.assertIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 1)

    def test_set_flag_doesnt_change_anything_if_tile_has_been_opened(self):
        self.minesw.showntiles[1] = 10
        self.minesw.grid.mines = 2
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.showntiles[1], 10)
        self.assertNotIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 0)

    def test_remove_flag_works(self):
        self.minesw.grid.mines = 1
        self.minesw.set_flag(1)
        self.minesw.remove_flag(1)
        self.assertEqual(self.minesw.showntiles[1], "_")
        self.assertNotIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 0)

    def test_remove_flag_doesnt_change_tile_if_tile_has_been_opened(self):
        self.minesw.showntiles[1] = 10
        self.minesw.remove_flag(1)
        self.assertEqual(self.minesw.showntiles[1], 10)

    def test_index_has_flag_returns_F_if_flag(self):
        self.minesw.grid.mines = 1
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.index_has_flag(1), "F")

    def test_index_has_flag_returns_False_if_no_flag(self):
        self.assertFalse(self.minesw.index_has_flag(1))
