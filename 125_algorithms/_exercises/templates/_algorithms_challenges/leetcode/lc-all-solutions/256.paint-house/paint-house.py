class Solution(object
  ___ minCost(self, costs
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    __ not costs:
      r_ 0
    dp = [0] * (le.(costs[0]))
    dp[:] = costs[0]
    ___ i in range(1, le.(costs)):
      d0 = d1 = d2 = 0
      ___ j in range(0, 3
        __ j __ 0:
          d0 = min(dp[1], dp[2]) + costs[i][0]
        ____ j __ 1:
          d1 = min(dp[0], dp[2]) + costs[i][1]
        ____
          d2 = min(dp[0], dp[1]) + costs[i][2]
      dp[0], dp[1], dp[2] = d0, d1, d2
    r_ min(dp)
