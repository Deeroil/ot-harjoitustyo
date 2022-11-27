from random import shuffle
from math import sqrt, pow

# turn into a class later?

# n = number of rows and columns
# list that equals a n*n matrix
# TODO: rename?


class Grid:
    def __init__(self, n):
        self.grid = []
        self.width = n
        self.len = n**2
        for i in range(n**2):
            self.grid.append(0)

    # TODO: add errorhandling or smth
    def set_mines(self, n):
        if len(self.grid) < n or n < 0:
            print('errorhandling here')
            return

        for i in range(0, n):
            self.grid[i] = 9  # 9 = a mine

        shuffle(self.grid)

    # TODO: fix this, there's some problems
    def count_neighbors(self, index):
        # index is not its own neighbor
        # do I want this to be hard-coded?
        neighbor_indexes = [index - self.width - 1, index - self.width, index - self.width + 1,
                            index - 1, index + 1,
                            index + self.width - 1, index + self.width, index + self.width + 1]
        # print(neighbor_indexes)

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
            if (self.grid[i] == 9):
                continue
            self.grid[i] = self.count_neighbors(i)
        # print("laskettu")
        # return self.grid

    # TODO: fix this
    # laittaa nyt ihan vääriä lukuja matriisiin, mutta en jaksa fiksaa heti
    # muokkaa __str__ -metodiksi?
    def print_as_matrix(self):
        n = self.width
        print('n on:', n)
        matrix = [[0 for i in range(n)] for j in range(n)]

        for i in range(len(self.grid) - 1):
            for j in range(n):
                for k in range(n):
                    matrix[j][k] = self.grid[i]
                    # print(matrix)

        for i in matrix:
            print(i)
