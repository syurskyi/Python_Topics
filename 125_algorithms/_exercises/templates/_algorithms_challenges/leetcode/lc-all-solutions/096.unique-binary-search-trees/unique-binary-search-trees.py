class Solution(object
  ___ _numTrees(self, n
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    ___ i in range(2, n + 1
      ___ j in range(1, i + 1
        dp[i] += dp[j - 1] * dp[i - j]
    r_ dp[-1]

  ___ numTrees(self, n
    ans = 1
    ___ i in range(1, n + 1
      ans = ans * (n + i) / i
    r_ ans / (n + 1)
