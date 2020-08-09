class Solution(object
  ___ minPathSum(self, grid
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    __ le.(grid) __ 0:
      r_ 0
    dp = [0 ___ _ in range(0, le.(grid[0]))]
    dp[0] = grid[0][0]

    ___ j in range(1, le.(grid[0])):
      dp[j] = dp[j - 1] + grid[0][j]

    ___ i in range(1, le.(grid)):
      pre = dp[0] + grid[i][0]
      ___ j in range(1, le.(grid[0])):
        dp[j] = min(dp[j], pre) + grid[i][j]
        pre = dp[j]
      dp[0] += grid[i][0]

    r_ dp[-1]
