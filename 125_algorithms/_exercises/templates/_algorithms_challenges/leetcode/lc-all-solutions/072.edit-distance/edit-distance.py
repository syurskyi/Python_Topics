c_ Solution(o..
  ___ minDistance  word1, word2
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    __ l..(word1) __ 0 o. l..(word2) __ 0:
      r.. m..(l..(word1), l..(word2

    dp [[0] * (l..(word2) + 1) ___ _ __ r..(0, l..(word1) + 1)]
    dp 0 0  0

    ___ i __ r..(0, l..(word1) + 1
      ___ j __ r..(0, l..(word2) + 1
        __ i __ 0:
          dp[i][j] j
        ____ j __ 0:
          dp[i][j] i
        ____
          cond1 dp[i][j - 1] + 1
          cond2 dp[i - 1][j] + 1
          cond3 0
          __ word1[i - 1] __ word2[j - 1]:
            cond3 dp[i - 1][j - 1]
          ____
            cond3 dp[i - 1][j - 1] + 1
          dp[i][j] m..(cond1, cond2, cond3)
    r.. dp[-1][-1]
