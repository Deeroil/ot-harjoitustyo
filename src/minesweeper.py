from grid import Grid

### TODO: onks mitkä näistä käli-asioita? uh oh

class Minesweeper:
    def __init__(self, grid: Grid):
        self.backgrid = grid
        self.showindexes = []
        for _ in range(grid.width**2):
            self.showindexes.append("_")

    # muista selittää että indeksointi alkaa 0:sta ja ylävasemmasta kulmasta TAI muuta näitä
    def check_tile(self, x: int, y: int):
        index = x + y*self.backgrid.width
        print(f"in tile ({x}, {y}) is number {self.backgrid.grid[index]}")
        return self.backgrid.grid[index]

    def add_shown_tiles(self, index):
      number = self.backgrid.grid[index]
      self.showindexes[index] = number

      number = self.backgrid.grid[index]

      # siirränää pois täältä
      if number == 9:
          print("Hävisit pelin :(")
          quit() #tää huono?
      elif number == 0:
          print("ööh mun pitää keksiä tähän algo :D")

    def __str__(self):
        bgrid = self.backgrid
        x = ""
        for i in range(bgrid.len):
            if i % bgrid.width == 0:
                x += "\n"
            x += f" {self.showindexes[i]} "
        print(x)