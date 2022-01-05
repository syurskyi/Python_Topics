c_ Solution(o..):
  ___ minCostII  costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    __ n.. costs:
      r.. 0
    dp = [[0] * l..(costs[0]) ___ _ __ r..(0, l..(costs))]
    dp[0] = costs[0]
    ___ i __ r..(1, l..(costs)):
      ___ j __ r..(0, l..(costs[0])):
        dp[i][j] = m..(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
    r.. m..(dp[-1])
