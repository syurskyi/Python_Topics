class Solution(object):
  ___ maxVacationDays(self, flights, days):
    """
    :type flights: List[List[int]]
    :type days: List[List[int]]
    :rtype: int
    """
    ans = 0
    dp = [[float("-inf")] * l..(flights) ___ _ __ r..(2)]
    dp[0][0] = 0
    ___ i __ r..(l..(days[0])):
      ___ j __ r..(l..(flights)):
        ___ k __ r..(l..(flights)):
          __ flights[k][j] __ 1 o. j __ k:
            dp[(i + 1) % 2][j] = max(dp[(i + 1) % 2][j], dp[i % 2][k] + days[j][i])
    r.. max(dp[l..(days[0]) % 2])
