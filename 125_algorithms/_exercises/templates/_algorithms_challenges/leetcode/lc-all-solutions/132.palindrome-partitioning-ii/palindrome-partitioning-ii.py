c_ Solution(o..
  ___ minCut  s
    """
    :type s: str
    :rtype: int
    """
    pal [[F.. ___ j __ r..(0, l..(s] ___ i __ r..(0, l..(s]
    dp [l..(s) ___ _ __ r..(0, l..(s) + 1)]
    ___ i __ r..(0, l..(s:
      ___ j __ r..(0, i + 1
        __ (s[i] __ s[j]) a.. ((j + 1 > i - 1) o. (pal[i - 1][j + 1]:
          pal[i][j] T..
          dp[i + 1] m..(dp[i + 1], dp[j] + 1) __ j !_ 0 ____ 0
    r.. dp[-1]
