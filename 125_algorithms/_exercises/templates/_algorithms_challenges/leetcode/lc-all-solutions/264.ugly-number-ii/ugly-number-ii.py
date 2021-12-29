class Solution(object):
  ___ nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    i2 = i3 = i5 = 1
    ___ i __ r..(2, n + 1):
      dp[i] = m..(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
      __ dp[i] __ dp[i2] * 2:
        i2 += 1
      __ dp[i] __ dp[i3] * 3:
        i3 += 1
      __ dp[i] __ dp[i5] * 5:
        i5 += 1
    r.. dp[-1]
