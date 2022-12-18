import sys
from services.errors import InvalidGridSize, InvalidMineAmount
from services.grid import Grid
from services.minesweeper import Minesweeper

### TODO:
#     - function for replaying

# command line interface
class CLI:
  """Command-line interface for Minesweeper.

  """
  def __init__(self):
    try:
      n = int(input(
          "Minkä kokoinen ruudukko (sivun pituus)? (pitää olla välillä [3...30]), muuten ohjelma suljetaan"))
      self.grid = Grid(n)
      m = int(input("Montako miinaa? (pitää olla välillä [1...ruudukossa olevat paikat], muuten ohjelma suljetaan)"))
      self.grid.set_mines(m)
    except (InvalidGridSize, InvalidMineAmount):
      "Annettu luku oli väärällä välillä, suljetaan ohjelma"
      sys.exit(0)
    except ValueError:
      print("Ei ollut numero! Suljetaan ohjelma")
      sys.exit(0)

    self.grid.set_neighbors()
    print("\n")
    self.msweep = Minesweeper(self.grid)

  def ask_coordinates(self):
    """Asks for x and y coordinates from user, transforms to an index of the grid.

      Returns:
        index created from x, y.
    """
    try:
      x_koord = int(input("Mikä x-koordinaatti? "))
      y_koord = int(input("Mikä y-koordinaatti? "))
    except ValueError:
      print("Ei ollut sopiva syöte! Anna sopiva kokonaisluku")

    index = x_koord + y_koord*self.grid.width
    return index

  # ensimmäisen kierroksen tarkistus
  # jos osuu pommiin, tehdään uusi alkutilanne jossa ei häviä heti
  # TODO: rename function to something shorter
  def generate_new_game_if_hit_bomb(self, index):
    """Replaces grid with a new one if given index hit a mine.

      Checks the first opened tile for a mine. If game is immediately lost
      (hits a mine), a new grid is generated. If the new grid also has a mine
      in the same index, same action is performed for some tries. If 10 tries
      isn't enough, game is continued with the last grid and the game is lost.

      Args:
        index: index of the first opened tile
    """
    if self.msweep.check_tile(index) == 9:
      print("osuttiin pommiin jo")
      for i in range(10):
        print("...generoidaan toinen ruudukko")
        grid2 = Grid(self.grid.width)
        grid2.set_mines(self.grid.mines)

        if grid2.list[index] != 9:
          grid2.set_neighbors()
          self.grid = grid2
          self.msweep = Minesweeper(grid2)
          break

  #maybe rename this as well
  def handle_flags(self, input, index):
    """Sets or removes a flag from given index if input is correct.

      Checks user input for "F" (add flag) or "R" (remove flag).
      Then handles flags according to the given input.

      Args:
        input: user input
        index: index of a tile
    """
    if input == "F":
      self.msweep.set_flag(index)

    elif input == "R":
      self.msweep.remove_flag(index)

  def play(self):
    """Command-line interface for Minesweeper in Finnish.

    """
    print("Tervetuloa pelaamaan miinaharavaa! Anna koordinaatit niin voit avata ruudun.")
    print("Koordinaattien numerointi alkaa 0:sta ja ylävasemmalta.")

    while True:
      try:
        index = self.ask_coordinates()
      except:
        continue
      break # user input was correct

    self.generate_new_game_if_hit_bomb(index) #for the first round

    self.msweep.add_shown_tiles(index)
    print(self.msweep.current_state())

    while True:
        if self.msweep.check_win():
          print("Voitit pelin!")
          cont = input("Kirjoita y aloittaaksesi alusta, muulla syötteellä suljet pelin")
          if cont == "y":
            self.__init__()
          else:
            sys.exit(0)

        if self.msweep.check_loss():
          print("Hävisit pelin :(")
          print(str(self.msweep.grid))
          sys.exit(0)

        inp = input("Kirjoita F asettaaksesi lipun tai R poistaaksesi lipun. Muulla syötteellä skipataan lipun asettaminen")
        try:
          index = self.ask_coordinates()
        except:
          continue

        if inp == "F" or inp == "R":
          self.handle_flags(inp, index)
          print(self.msweep.current_state())
          continue

        tile = self.msweep.check_tile(index)
        #0 is falsy so != doesnt work
        if tile is not False:
          self.msweep.add_shown_tiles(index)
          print(self.msweep.current_state())