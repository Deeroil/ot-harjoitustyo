from random import shuffle

class Grid:
    def __init__(self, width):
        self.grid = []
        self.width = width
        self.len = width**2
        for _ in range(width**2):
            self.grid.append(0)

    # TODO: add errorhandling or smth
    def set_mines(self, amount):
        if len(self.grid) < amount or amount < 0:
            print('errorhandling here')
            return

        for i in range(0, amount):
            self.grid[i] = 9  # 9 = a mine

        shuffle(self.grid)

    # TODO
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
            if self.grid[i] == 9:
                continue
            self.grid[i] = self.count_neighbors(i)
        # print("laskettu")
        # return self.grid

    # TODO
    # laittaa nyt ihan vääriä lukuja matriisiin, mutta en jaksa fiksaa heti
    # muokkaa __str__ -metodiksi?
    def print_as_matrix(self):
        wid = self.width
        print('width on:', wid)
        matrix = [[0 for _ in range(wid)] for _ in range(wid)]

        for i in range(len(self.grid) - 1):
            for j in range(wid):
                for k in range(wid):
                    matrix[j][k] = self.grid[i]
                    # print(matrix)

        for i in matrix:
            print(i)
