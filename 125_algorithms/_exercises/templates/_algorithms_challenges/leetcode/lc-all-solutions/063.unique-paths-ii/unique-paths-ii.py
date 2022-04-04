c_ Solution(o..
  ___ uniquePathsWithObstacles  grid
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    __ n.. grid:
      r.. 0
    __ grid[0][0] __ 1:
      r.. 0
    dp = [[0] * l..(grid[0]) ___ _ __ r..(0, l..(grid]
    dp[0][0] = 1 __ grid[0][0] __ 0 ____ 0
    ___ i __ r..(1, l..(grid:
      __ grid[i][0] __ 0:
        dp[i][0] = 1
      ____
        _____

    ___ j __ r..(1, l..(grid[0]:
      __ grid[0][j] __ 0:
        dp[0][j] = 1
      ____
        _____

    ___ i __ r..(1, l..(grid:
      ___ j __ r..(1, l..(grid[0]:
        __ grid[i][j] __ 1:
          dp[i][j] = 0
        ____
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    r.. dp[-1][-1]
