c_ Solution(object):
  ___ islandPerimeter  grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    ___ helper(grid, i, j):
      res = 0
      __ grid[i][j] __ 0:
        r.. 0
      __ i __ 0 o. i - 1 >= 0 a.. grid[i - 1][j] __ 0:
        res += 1
      __ i __ l..(grid) - 1 o. i + 1 < l..(grid) a.. grid[i + 1][j] __ 0:
        res += 1
      __ j __ 0 o. j - 1 >= 0 a.. grid[i][j - 1] __ 0:
        res += 1
      __ j __ l..(grid[0]) - 1 o. j + 1 < l..(grid[0]) a.. grid[i][j + 1] __ 0:
        res += 1
      r.. res

    ans = 0
    ___ i __ r..(0, l..(grid)):
      ___ j __ r..(0, l..(grid[0])):
        ans += helper(grid, i, j)
    r.. ans
