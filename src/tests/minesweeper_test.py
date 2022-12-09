import unittest
from services.grid import Grid
from services.minesweeper import Minesweeper


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.test_grid = Grid(3)
        self.test_grid.list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.minesw = Minesweeper(self.test_grid)

    # check tile
    def test_check_tile_1_2(self):
        self.assertEqual(self.minesw.check_tile(7), 7)

    def test_check_tile_0_0(self):
        self.assertEqual(self.minesw.check_tile(0), 0)
    
    def test_check_tile_doesnt_work_with_negative_index(self):
        self.assertFalse(self.minesw.check_tile(-2))

    def test_check_tile_false(self):
        self.assertFalse(self.minesw.check_tile(0), 10)

    # check index viability
    def test_check_index_viability_with_neg_one_returns_False(self):
        self.assertFalse(self.minesw.check_index_viability(-1))
    
    def test_check_index_viability_with_too_big_index_returns_False(self):
        self.assertFalse(self.minesw.check_index_viability(10))

    def test_check_index_viability_with_too_big_index_returns_False(self):
        self.assertFalse(self.minesw.check_index_viability(10))

    #flag tests
    def test_set_flag_works_on_unopened_tile_when_grid_has_mines(self):
        self.minesw.grid.mines = 2
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), "F")
        self.assertIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 1)

    def test_set_flag_doesnt_set_if_no_mines(self):
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), "_")
        self.assertNotIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 0)   

    def test_set_flag_doesnt_set_if_not_enough_mines_left(self):
        self.minesw.grid.mines = 1
        self.minesw.set_flag(1)
        self.minesw.set_flag(2)
        self.assertEqual(self.minesw.get_shown_tile(2), "_")
        self.assertNotIn(2, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 1)

    def test_set_flag_doesnt_change_anything_if_flag_exists(self):
        self.minesw.grid.mines = 2
        self.minesw.set_flag(1)
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), "F")
        self.assertIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 1)

    def test_set_flag_doesnt_change_anything_if_tile_has_been_opened(self):
        self.minesw.grid.list[1] = 10
        self.minesw.showntiles.add(1)
        self.minesw.grid.mines = 2
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), 10)
        self.assertNotIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 0)

    def test_remove_flag_works(self):
        self.minesw.grid.mines = 1
        self.minesw.set_flag(1)
        self.minesw.remove_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), "_")
        self.assertNotIn(1, self.minesw.flags)
        self.assertEqual(len(self.minesw.flags), 0)

    def test_remove_flag_doesnt_change_tile_if_tile_has_been_opened(self):
        self.minesw.grid.list[1] = 10
        self.minesw.showntiles.add(1)
        self.minesw.remove_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), 10)

    # get shown tiles
    def test_get_shown_tiles_index_2_is_underscore(self):
        self.assertEqual(self.minesw.get_shown_tile(2), "_")

    def test_get_shown_tile_returns_right_number(self):
        self.minesw.add_shown_tiles(3)
        self.assertEqual(self.minesw.get_shown_tile(3), 3)
    
    def test_get_shown_tile_returns_right_number2(self):
        self.minesw.grid.list[1] = 10
        self.minesw.add_shown_tiles(1)
        self.assertEqual(self.minesw.get_shown_tile(1), 10)

    def test_get_shown_tile_returns_F_if_flag(self):
        self.minesw.grid.mines = 1
        self.minesw.set_flag(1)
        self.assertEqual(self.minesw.get_shown_tile(1), "F")