class Solution(object
  ___ maxKilledEnemies(self, grid
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    __ not grid:
      r_ 0
    dpRow = [[0] * (le.(grid[0]) + 2) ___ _ in range(0, le.(grid) + 2)]
    dpCol = [[0] * (le.(grid[0]) + 2) ___ _ in range(0, le.(grid) + 2)]

    ___ i in range(0, le.(grid)):
      ___ j in range(0, le.(grid[0])):
        dpRow[i + 1][j + 1] = dpRow[i + 1][j]
        dpCol[i + 1][j + 1] = dpCol[i][j + 1]
        __ grid[i][j] __ "W":
          dpRow[i + 1][j + 1] = 0
          dpCol[i + 1][j + 1] = 0
        __ grid[i][j] __ "E":
          dpRow[i + 1][j + 1] += 1
          dpCol[i + 1][j + 1] += 1

    maxKilled = 0
    ___ i in reversed(range(0, le.(grid))):
      ___ j in reversed(range(0, le.(grid[0]))):
        __ grid[i][j] __ "W":
          continue
        dpRow[i + 1][j + 1] = max(dpRow[i + 1][j + 1], dpRow[i + 1][j + 2])
        dpCol[i + 1][j + 1] = max(dpCol[i + 1][j + 1], dpCol[i + 2][j + 1])
        __ grid[i][j] __ "0":
          maxKilled = max(maxKilled, dpRow[i + 1][j + 1] + dpCol[i + 1][j + 1])
    r_ maxKilled
