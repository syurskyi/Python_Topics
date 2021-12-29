class Solution(object):
  ___ minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    __ l..(grid) __ 0:
      r.. 0
    dp = [0 ___ _ __ r..(0, l..(grid[0]))]
    dp[0] = grid[0][0]

    ___ j __ r..(1, l..(grid[0])):
      dp[j] = dp[j - 1] + grid[0][j]

    ___ i __ r..(1, l..(grid)):
      pre = dp[0] + grid[i][0]
      ___ j __ r..(1, l..(grid[0])):
        dp[j] = m..(dp[j], pre) + grid[i][j]
        pre = dp[j]
      dp[0] += grid[i][0]

    r.. dp[-1]
