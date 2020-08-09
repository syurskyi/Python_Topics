class Solution(object
  ___ islandPerimeter(self, grid
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    ___ helper(grid, i, j
      res = 0
      __ grid[i][j] __ 0:
        r_ 0
      __ i __ 0 or i - 1 >= 0 and grid[i - 1][j] __ 0:
        res += 1
      __ i __ le.(grid) - 1 or i + 1 < le.(grid) and grid[i + 1][j] __ 0:
        res += 1
      __ j __ 0 or j - 1 >= 0 and grid[i][j - 1] __ 0:
        res += 1
      __ j __ le.(grid[0]) - 1 or j + 1 < le.(grid[0]) and grid[i][j + 1] __ 0:
        res += 1
      r_ res

    ans = 0
    for i in range(0, le.(grid)):
      for j in range(0, le.(grid[0])):
        ans += helper(grid, i, j)
    r_ ans
