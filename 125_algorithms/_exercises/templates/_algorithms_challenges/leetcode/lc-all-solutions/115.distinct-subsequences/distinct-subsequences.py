class Solution(object
  # space O(n^2)
  ___ _numDistinct(self, s, t
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0] * (le.(t) + 1) ___ _ in range(0, le.(s) + 1)]

    ___ i in range(0, le.(s) + 1
      dp[i][0] = 1

    ___ i in range(1, le.(s) + 1
      ___ j in range(1, le.(t) + 1
        dp[i][j] += dp[i - 1][j]
        __ t[j - 1] __ s[i - 1]:
          dp[i][j] += dp[i - 1][j - 1]

    r_ dp[-1][-1]

  ___ numDistinct(self, s, t
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [0] * (le.(t) + 1)
    ___ i in range(1, le.(s) + 1
      pre = 1
      ___ j in range(1, le.(t) + 1
        tmp = dp[j]
        __ t[j - 1] __ s[i - 1]:
          dp[j] += pre
        pre = tmp
    r_ dp[-1]
