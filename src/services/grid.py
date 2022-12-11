from random import shuffle


class Grid:
    def __init__(self, width):
        self.list = []
        self.width = width
        self.len = width**2
        for _ in range(width**2):
            self.list.append(0)
        self.mines = 0

    def set_mines(self, amount):
        if len(self.list) < amount or amount < 0:
            print('errorhandling here')
            return
        self.mines = amount

        for i in range(0, amount):
            self.list[i] = 9  # 9 = a mine

        shuffle(self.list)

    def check_bounds(self, index):
        top_row = {index - self.width - 1, index - self.width, index - self.width + 1}
        middle_row = {index - 1, index + 1} #is this useless?
        bottom_row = {index + self.width - 1, index + self.width, index + self.width + 1}
        left_col = {index - self.width - 1, index - 1, index + self.width - 1}
        right_col = {index - self.width + 1, index + 1, index + self.width + 1}

        neighbor_indexes = set()
        neighbor_indexes.update(top_row, middle_row, left_col, right_col, bottom_row)

        #index on top row
        if 0 <= index <= self.width - 1:
            # print("index on top row")
            neighbor_indexes = neighbor_indexes - top_row

        #index on bottom row
        if self.len - self.width <= index <= self.len - 1:
            # print("index on bottom row")
            neighbor_indexes = neighbor_indexes - bottom_row

        #index on left column
        if index % self.width == 0:
            # print("index on left column")
            neighbor_indexes = neighbor_indexes - left_col

        #index on right column
        if index % self.width == self.width - 1:
            # print("index on right column")
            neighbor_indexes = neighbor_indexes - right_col

        return neighbor_indexes

    def count_neighbors(self, index):
        neighbor_indexes = self.check_bounds(index)

        mines = 0
        for i in neighbor_indexes:
            if i < 0 or i >= self.len:
                continue
            if self.list[i] == 9:
                # print("mine spotted in", i)
                mines += 1
        return mines

    def set_neighbors(self):
        for i in range(self.len):
            if self.list[i] == 9:
                continue
            self.list[i] = self.count_neighbors(i)

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
            printable += f" {self.list[i]} "
        print(printable)
