import unittest
from repository.save_file import SaveFile
from services.minesweeper import Minesweeper
from services.grid import Grid

class TestSaveFile(unittest.TestCase):
    def setUp(self):
        SaveFile.remove()
        
        self.msw = Minesweeper(Grid(3))
        self.msw.grid.list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.save = SaveFile(self.msw, 3)

    def test_save_creates_a_file(self):
      self.save.save()

      #TODO: tarkista onko tiedosto olemassa

    def test_load_returns_saved_file(self):
      self.save.save()
      loaded = self.save.load()

      self.assertEqual(loaded.minesweeper.grid.list, self.msw.grid.list)
      self.assertEqual(loaded.minesweeper.grid.mines, self.msw.grid.mines)
      self.assertEqual(loaded.minesweeper.showntiles, self.msw.showntiles)
      self.assertEqual(loaded.minesweeper.flags, self.msw.flags)
      self.assertEqual(loaded.wins, 3)
    
    def test_load_does_nothing_if_file_not_found(self):
      loaded = None
      loaded = self.save.load()

      self.assertEqual(loaded, None)

    def test_remove_destroys_file(self):
      self.save.remove()
      #TODO: tsekkaa ettei oo enää tiedostoa
