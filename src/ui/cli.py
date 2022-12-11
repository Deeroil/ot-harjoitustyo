import sys
from services.grid import Grid
from services.minesweeper import Minesweeper

### TODO:
#     - function for replaying

# command line interface
class CLI:
  def __init__(self):
    n = int(input(
        "Minkä kokoinen ruudukko (sivun pituus)? (0 tai vähemmän sulkee ohjelman) "))
    if n <= 0:
        sys.exit(0)
    m = int(input("Montako miinaa? (0 tai vähemmän sulkee ohjelman)"))
    if m <= 0:
        sys.exit(0)

    self.grid = Grid(n)
    self.grid.set_mines(m)
    self.grid.set_neighbors()
    # self.grid.print_grid()

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
      # TODO: laske esim 10 kertaa ja sitten lopeta jos ei onnistunut
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
      print(self.msweep.current_state())

    elif input == "R":
      self.msweep.remove_flag(index)
      print(self.msweep.current_state())

  def play(self):
    print("Tervetuloa pelaamaan miinaharavaa! Anna koordinaatit niin voit avata ruudun.")
    print("Koordinaattien numerointi alkaa 0:sta ja ylävasemmalta.")
    index = self.ask_coordinates()
    self.generate_new_game_if_hit_bomb(index) #for the first round

    self.msweep.add_shown_tiles(index)
    print(self.msweep.current_state()) # not for final release

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
          print(self.msweep.current_state())

          if tile == 9:
              print("Hävisit pelin :(")
              print(str(self.msweep.grid))
              sys.exit(0)
          elif tile == 0:
              print("(ei vielä avaa muita läheisiä 0-tiiliä)")

        # msweep.add_shown_tiles(0)
        # ei oo lopetusehtoa paitsi miinaan osuminen