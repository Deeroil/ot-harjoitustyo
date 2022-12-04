import sys
from services.grid import Grid
from services.minesweeper import Minesweeper

### TODO:
#     - function for replaying
#     - function for checking win condition? wait that sounds like game logic, no.

# command line interface
class CLI:
  def __init__(self):
    n = int(input(
        "Create a minesweeper grid of what size? (0 or less quits game) "))
    if n <= 0:
        sys.exit(0)
    m = int(input("And how many mines? (0 or less quits game) "))
    if m <= 0:
        sys.exit(0)

    self.grid = Grid(n)
    self.grid.set_mines(m)
    self.grid.set_neighbors()
    self.grid.print_grid()

    print("\n")
    self.msweep = Minesweeper(self.grid)

  def ask_coordinates(self):
    x_koord = int(input("Mikä x-koordinaatti? "))
    y_koord = int(input("Mikä y-koordinaatti? "))
    index = x_koord + y_koord*self.grid.width
    return index

  # ensimmäisen kierroksen tarkistus
  # jos osuu pommiin, tehdään uusi alkutilanne jossa ei häviä heti
  # TODO: rename function to something shorter
  def generate_new_game_if_hit_bomb(self, index):
    if self.msweep.check_tile(index) == 9:
      print("osuttiin pommiin jo")
      while True:
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
    if input == "F":
      self.msweep.set_flag(index)
      self.msweep.print_current()

    elif input == "R":
      self.msweep.remove_flag(index)
      self.msweep.print_current()

  def play(self):
    print("Tervetuloa pelaamaan miinaharavaa! Anna koordinaatit niin voit avata ruudun.")
    print("Koordinaattien numerointi alkaa 0:sta ja ylävasemmalta.")
    index = self.ask_coordinates()
    self.generate_new_game_if_hit_bomb(index) #for the first round

    self.msweep.add_shown_tiles(index)
    self.msweep.print_current() # not for final release

    while True:
        if self.msweep.check_win():
          print("Voitit pelin!")
          cont = input("Kirjoita y aloittaaksesi alusta, muulla syötteellä suljet pelin")
          if cont == "y":
            self.__init__()
          else:
            sys.exit(0)

        inp = input("Kirjoita F asettaaksesi lipun tai R poistaaksesi lipun. Muulla syötteellä skipataan lipun asettaminen")
        index = self.ask_coordinates()
        
        if inp == "F" or inp == "R":
          self.handle_flags(inp, index)
          continue

        tile = self.msweep.check_tile(index)

        if tile != False:
          self.msweep.add_shown_tiles(index)
          self.msweep.print_current()

          if tile == 9:
              print("Hävisit pelin :(")
              self.msweep.grid.print_grid()
              sys.exit(0)
          elif tile == 0:
              print("ööh mun pitää keksiä tähän algo :D sori siitä")

        # msweep.add_shown_tiles(0)
        # ei oo lopetusehtoa paitsi miinaan osuminen