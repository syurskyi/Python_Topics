class Solution(object
  ___ findMaxForm(self, strs, m, n
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[0] * (n + 1) ___ _ in range(0, m + 1)]
    ___ dj, dk in [(s.count("0"), s.count("1")) ___ s in strs]:
      ___ j in reversed(range(0, m + 1)):
        ___ k in reversed(range(0, n + 1)):
          __ j - dj >= 0 and k - dk >= 0:
            dp[j][k] = max(dp[j][k], dp[j - dj][k - dk] + 1)
    r_ dp[-1][-1]
