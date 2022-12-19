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

    # flag tests
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

    def test_current_state(self):
        compare_str = "\n 0  1  2 \n 3  4  5 \n 6  7  8 "
        self.minesw.grid.list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        for i in range(self.minesw.grid.len):
            self.minesw.add_shown_tiles(i)

        self.assertEqual(self.minesw.current_state(), compare_str)

    def test_find_nearby_zeros_works_for_zero_grid(self):
        compare_indices = {0, 1, 2, 3, 4, 5, 6, 7, 8}
        msw = Minesweeper(Grid(3))
        self.assertEqual(msw.find_nearby_zeros(0, set()), compare_indices)

    def test_find_nearby_zeros_works_1(self):
        msw = Minesweeper(Grid(4))
        msw.grid.list = [1, 1, 0, 0,
                         0, 1, 1, 0,
                         0, 0, 1, 0,
                         0, 1, 1, 1]
        compare_indices = {4, 8, 9, 12}
        self.assertEqual(msw.find_nearby_zeros(4, set()), compare_indices)

    def test_find_nearby_zeros_works_2(self):
        msw = Minesweeper(Grid(4))
        msw.grid.list = [1, 1, 0, 0,
                         0, 1, 1, 0,
                         0, 0, 1, 0,
                         0, 1, 1, 1]
        compare_indices = {2, 3, 7, 11}
        self.assertEqual(msw.find_nearby_zeros(3, set()), compare_indices)

    def test_single_zero(self):
        msw = Minesweeper(Grid(5))
        msw.grid.list = [9, 9, 9, 9, 9,
                         9, 0, 0, 0, 9,
                         9, 0, 0, 0, 9,
                         9, 0, 0, 0, 9,
                         9, 9, 9, 9, 9]
        msw.grid.set_neighbors()
        msw.add_shown_tiles(12)
        print('showntiles', msw.showntiles)
        self.assertEqual(msw.showntiles, {6, 7, 8, 11, 12, 13, 16, 17, 18})
        self.assertNotIn(0, msw.showntiles)

    def test_add_shown_tiles_adds_nearby_zeros_and_neighbors(self):
        msw = Minesweeper(Grid(3))
        msw.grid.list = [1, 0, 0,
                         1, 1, 0,
                         0, 1, 1]
        msw.add_shown_tiles(1)
        added_indices = {0, 1, 2, 3, 4, 5, 7, 8}
        self.assertEqual(msw.showntiles, added_indices)

    def test_add_shown_tiles_doesnt_add_all_zeros(self):
        msw = Minesweeper(Grid(3))
        msw.grid.list = [1, 0, 0,
                         1, 1, 0,
                         0, 1, 1]
        msw.add_shown_tiles(1)
        all_zero_indices = {1, 2, 5, 6}
        self.assertNotEqual(msw.showntiles, all_zero_indices)
        self.assertNotIn(6, msw.showntiles)
