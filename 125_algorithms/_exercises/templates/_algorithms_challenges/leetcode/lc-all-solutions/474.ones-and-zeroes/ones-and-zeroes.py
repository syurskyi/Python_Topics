c_ Solution(object):
  ___ findMaxForm(self, strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    dp = [[0] * (n + 1) ___ _ __ r..(0, m + 1)]
    ___ dj, dk __ [(s.c.. "0"), s.c.. "1")) ___ s __ strs]:
      ___ j __ reversed(r..(0, m + 1)):
        ___ k __ reversed(r..(0, n + 1)):
          __ j - dj >= 0 a.. k - dk >= 0:
            dp[j][k] = max(dp[j][k], dp[j - dj][k - dk] + 1)
    r.. dp[-1][-1]
