class Solution(object):
  ___ numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = set()
    ans = 0

    ___ dfs(grid, i, j, visited):
      __ i < 0 o. i >= l..(grid) o. j < 0 o. j >= l..(grid[0]) o. grid[i][j] __ "0" o. (i, j) __ visited:
        r.. False
      visited |= {(i, j)}
      ___ di, dj __ [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newi, newj = i + di, j + dj
        dfs(grid, newi, newj, visited)
      r.. True

    ___ i __ r..(0, l..(grid)):
      ___ j __ r..(0, l..(grid[0])):
        __ dfs(grid, i, j, visited):
          ans += 1
    r.. ans
