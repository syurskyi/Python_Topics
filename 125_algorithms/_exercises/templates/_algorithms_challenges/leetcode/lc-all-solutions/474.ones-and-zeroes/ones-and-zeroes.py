c_ Solution(o..
  ___ findMaxForm  strs, m, n
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    dp [[0] * (n + 1) ___ _ __ r..(0, m + 1)]
    ___ dj, dk __ [(s.c.. "0"), s.c.. "1" ___ s __ strs]:
      ___ j __ r..(r..(0, m + 1:
        ___ k __ r..(r..(0, n + 1:
          __ j - dj >_ 0 a.. k - dk >_ 0:
            dp[j][k] m..(dp[j][k], dp[j - dj][k - dk] + 1)
    r.. dp[-1][-1]
