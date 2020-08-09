class Solution(object
  ___ minCostII(self, costs
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    __ not costs:
      r_ 0
    dp = [[0] * le.(costs[0]) ___ _ in range(0, le.(costs))]
    dp[0] = costs[0]
    ___ i in range(1, le.(costs)):
      ___ j in range(0, le.(costs[0])):
        dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
    r_ min(dp[-1])
