class Solution(object
  ___ uniquePathsWithObstacles(self, grid
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    __ not grid:
      r_ 0
    __ grid[0][0] __ 1:
      r_ 0
    dp = [[0] * le.(grid[0]) ___ _ in range(0, le.(grid))]
    dp[0][0] = 1 __ grid[0][0] __ 0 else 0
    ___ i in range(1, le.(grid)):
      __ grid[i][0] __ 0:
        dp[i][0] = 1
      ____
        break

    ___ j in range(1, le.(grid[0])):
      __ grid[0][j] __ 0:
        dp[0][j] = 1
      ____
        break

    ___ i in range(1, le.(grid)):
      ___ j in range(1, le.(grid[0])):
        __ grid[i][j] __ 1:
          dp[i][j] = 0
        ____
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    r_ dp[-1][-1]
