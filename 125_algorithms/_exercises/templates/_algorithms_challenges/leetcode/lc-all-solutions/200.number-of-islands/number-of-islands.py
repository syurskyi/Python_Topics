c_ Solution(o..
  ___ numIslands  grid
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = s..()
    ans = 0

    ___ dfs(grid, i, j, visited
      __ i < 0 o. i >_ l..(grid) o. j < 0 o. j >_ l..(grid[0]) o. grid[i][j] __ "0" o. (i, j) __ visited:
        r.. F..
      visited |= {(i, j)}
      ___ di, dj __ [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newi, newj = i + di, j + dj
        dfs(grid, newi, newj, visited)
      r.. T..

    ___ i __ r..(0, l..(grid:
      ___ j __ r..(0, l..(grid[0]:
        __ dfs(grid, i, j, visited
          ans += 1
    r.. ans
