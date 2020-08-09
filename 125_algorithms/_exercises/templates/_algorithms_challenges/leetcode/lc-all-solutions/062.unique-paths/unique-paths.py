class Solution(object
  ___ uniquePaths(self, m, n
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [1] * n

    ___ i in range(1, m
      pre = 1
      ___ j in range(1, n
        dp[j] = dp[j] + pre
        pre = dp[j]
    r_ dp[-1]
