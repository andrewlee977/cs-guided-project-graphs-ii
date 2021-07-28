"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
def numIslands(grid):
    # Your code here
    # if the grid is empty or none
    if grid is None or len(grid) == 0:
      # return zero
      return 0
    
    # get max rows
    MAX_ROWS = len(grid)
    # get max cols
    MAX_COLS = len(grid[0])
    # keep track of number of islands
    num_islands = 0

    # iterate over all rows
    for row in range(MAX_ROWS):
      # iterate over all cols
      for col in range(MAX_COLS):
        # check if grid at row and col is "1"
        if grid[row][col] == "1":
          # increment the number of islands
          num_islands += 1
          # mark it as visited
          grid[row][col] = "V"
          # create a queue to hold the neighbors to visit
          neighbors = []
          # add the gridsquare at row * MAX_COLS + col
          neighbors.append(row * MAX_COLS + col)
          # while there are still neighbors
          while len(neighbors) > 0:
            # dequeue the current neighbor
            id = neighbors.pop(0)
            # calculate current row by using an algorithm of row = id // MAX_COLS
            row = id // MAX_COLS
            # calculate the current col by using the algorithm col = id % MAX_COLS
            col = id % MAX_COLS
            # check the row - 1 is greater than or equal to zero
            # and grid at row - 1 and col is equal to "1"
            if row - 1 >= 0 and grid[row - 1][col] == "1":
              # mark the neighbor as visited and add to neighbors
              neighbors.append((row - 1) * MAX_COLS + col)
              grid[row - 1][col] = "V"

            # check if row + 1 is less than MAX_ROWS and is equal to "1"
            if row + 1 < MAX_ROWS and grid[row + 1][col] == "1":
              # mark the neighbor as visited
              neighbors.append((row + 1) * MAX_COLS + col)
              grid[row + 1][col] = "V"
            # check col - 1 is greater than zero and is equal to "1"
            if col - 1 >= 0 and grid[row][col - 1] == "1":
              # mark the neighbor as visited
              neighbors.append(row * MAX_COLS + col - 1)
              grid[row][col - 1] = "V"
            # check col + 1 is less than the MAX_COLS and is equal to "1"
            if col + 1 < MAX_COLS and grid[row][col + 1] == "1":
              # mark the neighbor as visited
              neighbors.append(row * MAX_COLS + col + 1)
              grid[row][col + 1] = "V"
    # return the island count
    return num_islands

