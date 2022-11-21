from random import shuffle
from math import sqrt, pow

# turn into a class later?

# n = number of rows and columns
# list that equals a n*n matrix
# TODO: rename?

def grid_list(n):
  list = []
  n = int(pow(n, 2))
  for i in range(n):
    list.append(0)
  # print('length', len(list))
  return list

# TODO: add errorhandling or smth
def set_mines(grid_list, n):
  if len(grid_list) < n or n < 0:
    print('errorhandling here')
    return grid_list

  for i in range(0, n):
    grid_list[i] = 9 # 9 = a mine

  shuffle(grid_list)
  return grid_list

# TODO: fix this, there's some problems
def count_neighbors(grid_list, index):
  row_len = int(sqrt(len(grid_list)))
  # print('row_len', row_len)

  # index is not its own neighbor
  # do I want this to be hard-coded?
  neighbor_indexes = [index - row_len - 1, index - row_len, index - row_len + 1,
                      index - 1, index + 1,
                      index + row_len - 1, index + row_len, index + row_len + 1]
  # print(neighbor_indexes)

  mines = 0
  for i in neighbor_indexes:
    if i < 0 or i >= len(grid_list):
      continue
    if grid_list[i] == 9:
      # print("mine spotted in", i)
      mines += 1
  return mines

# muista testata ettei miinojen päälle aseteta numeroita!
def set_neighbors(grid_list):
  for i in range(len(grid_list)):
    if(grid_list[i] == 9):
      continue
    grid_list[i] = count_neighbors(grid_list, i)
  # print("laskettu")
  return grid_list

# TODO: fix this
# laittaa nyt ihan vääriä lukuja matriisiin, mutta en jaksa fiksaa heti
def print_as_matrix(grid_list):
  n = int(sqrt(len(grid_list)))
  print('n on:', n)
  matrix = [[0 for i in range(n)] for j in range(n)]

  for i in range(len(grid_list) - 1):
    for j in range(n):
      for k in range(n):
        matrix[j][k] = grid_list[i]
        # print(matrix)

  for i in matrix:
    print(i)
