class Solution(object
  ___ maxVacationDays(self, flights, days
    """
    :type flights: List[List[int]]
    :type days: List[List[int]]
    :rtype: int
    """
    ans = 0
    dp = [[float("-inf")] * le.(flights) ___ _ in range(2)]
    dp[0][0] = 0
    ___ i in range(le.(days[0])):
      ___ j in range(le.(flights)):
        ___ k in range(le.(flights)):
          __ flights[k][j] __ 1 or j __ k:
            dp[(i + 1) % 2][j] = max(dp[(i + 1) % 2][j], dp[i % 2][k] + days[j][i])
    r_ max(dp[le.(days[0]) % 2])
