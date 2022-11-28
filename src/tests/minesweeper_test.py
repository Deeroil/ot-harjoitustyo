import unittest
from grid import Grid
from minesweeper import Minesweeper

class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        # self.grid = Grid(5)
        self.test_grid = Grid(3)
        self.test_grid.grid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.minesw = Minesweeper(self.test_grid)

    def test_check_tile_1_2(self):
        self.assertEqual(self.minesw.check_tile(1, 2), 7)

    def test_check_tile_0_0(self):
        self.assertEqual(self.minesw.check_tile(0, 0), 0)

    def test_check_tile_false(self):
        self.assertFalse(self.minesw.check_tile(0, 0), 10)        
