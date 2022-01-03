c_ Solution(object):
  ___ minCost(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    __ n.. costs:
      r.. 0
    dp = [0] * (l..(costs[0]))
    dp |  = costs[0]
    ___ i __ r..(1, l..(costs)):
      d0 = d1 = d2 = 0
      ___ j __ r..(0, 3):
        __ j __ 0:
          d0 = m..(dp[1], dp[2]) + costs[i][0]
        ____ j __ 1:
          d1 = m..(dp[0], dp[2]) + costs[i][1]
        ____:
          d2 = m..(dp[0], dp[1]) + costs[i][2]
      dp[0], dp[1], dp[2] = d0, d1, d2
    r.. m..(dp)
