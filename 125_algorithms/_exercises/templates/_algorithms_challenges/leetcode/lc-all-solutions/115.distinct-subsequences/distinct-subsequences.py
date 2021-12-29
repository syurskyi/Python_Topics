class Solution(object):
  # space O(n^2)
  ___ _numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [[0] * (l..(t) + 1) ___ _ __ r..(0, l..(s) + 1)]

    ___ i __ r..(0, l..(s) + 1):
      dp[i][0] = 1

    ___ i __ r..(1, l..(s) + 1):
      ___ j __ r..(1, l..(t) + 1):
        dp[i][j] += dp[i - 1][j]
        __ t[j - 1] __ s[i - 1]:
          dp[i][j] += dp[i - 1][j - 1]

    r.. dp[-1][-1]

  ___ numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    dp = [0] * (l..(t) + 1)
    ___ i __ r..(1, l..(s) + 1):
      pre = 1
      ___ j __ r..(1, l..(t) + 1):
        tmp = dp[j]
        __ t[j - 1] __ s[i - 1]:
          dp[j] += pre
        pre = tmp
    r.. dp[-1]
