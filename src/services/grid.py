from random import shuffle


class Grid:
    def __init__(self, width):
        self.grid = []
        self.width = width
        self.len = width**2
        for _ in range(width**2):
            self.grid.append(0)
        self.mines = 0

    # TODO: add errorhandling or smth
    def set_mines(self, amount):
        if len(self.grid) < amount or amount < 0:
            print('errorhandling here')
            return
        self.mines = amount

        for i in range(0, amount):
            self.grid[i] = 9  # 9 = a mine

        shuffle(self.grid)

    def check_bounds(self, index):
        top_row = {index - self.width - 1, index - self.width, index - self.width + 1}
        middle_row = {index - 1, index + 1} #is this useless?
        bottom_row = {index + self.width - 1, index + self.width, index + self.width + 1}
        left_col = {index - self.width - 1, index - 1, index + self.width - 1}
        right_col = {index - self.width + 1, index + 1, index + self.width + 1}

        neighbor_indexes = set()
        neighbor_indexes.update(top_row, middle_row, left_col, right_col, bottom_row)

        #index on top row
        if 0 <= index <= self.width - 1: #huh, 3x3-matriisissa 3 luuli olevansa täällä ehkä koska <= width?
            print("index on top row")
            neighbor_indexes = neighbor_indexes - top_row

        #index on bottom row
        if (self.len - 1) - self.width <= index <= self.len - 1: #TODO: TARKISTA TÄÄ
            print("index on bottom row")
            neighbor_indexes = neighbor_indexes - bottom_row
        
        #index on left column
        if index % self.width == 0:
            print("index on left column")
            neighbor_indexes = neighbor_indexes - left_col

        #index on right column
        if index % 3 == 2: #TODO: CHECK THIS, toimi 3x3 gridille mutta en tiedä toimiiko oikeasti
            print("index on right column")
            neighbor_indexes = neighbor_indexes - right_col

        return neighbor_indexes


    # TODO
    def count_neighbors(self, index):
        neighbor_indexes = self.check_bounds(index)

        mines = 0
        for i in neighbor_indexes:
            if i < 0 or i >= self.len:
                continue
            if self.grid[i] == 9:
                # print("mine spotted in", i)
                mines += 1
        return mines

    # muista testata ettei miinojen päälle aseteta numeroita!
    def set_neighbors(self):
        for i in range(self.len):
            if self.grid[i] == 9:
                continue
            self.grid[i] = self.count_neighbors(i)
        # print("laskettu")
        # return self.grid

# tulostaa grid jossa näkyy naapurit, tyhjät ja pommit
#   0: tyhjä
#   1-8: montako pomminaapuria
#   9: pommi/miina
# TODO: rename printable
    def print_grid(self):
        printable = ""
        for i in range(self.len):
            if i % self.width == 0:
                printable += "\n"
            printable += f" {self.grid[i]} "
        print(printable)
