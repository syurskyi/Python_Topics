class Solution(object
  ___ numIslands(self, grid
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = set()
    ans = 0

    ___ dfs(grid, i, j, visited
      __ i < 0 or i >= le.(grid) or j < 0 or j >= le.(grid[0]) or grid[i][j] __ "0" or (i, j) in visited:
        r_ False
      visited |= {(i, j)}
      ___ di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newi, newj = i + di, j + dj
        dfs(grid, newi, newj, visited)
      r_ True

    ___ i in range(0, le.(grid)):
      ___ j in range(0, le.(grid[0])):
        __ dfs(grid, i, j, visited
          ans += 1
    r_ ans
