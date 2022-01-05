c_ Solution(o..):
  ___ minDistance  word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    dp = [[0] * (l..(word2) + 1) ___ _ __ r..(l..(word1) + 1)]
    ___ i __ r..(1, l..(word2) + 1):
      dp[0][i] = i
    ___ i __ r..(1, l..(word1) + 1):
      dp[i][0] = i

    ___ i __ r..(l..(word1)):
      ___ j __ r..(l..(word2)):
        __ word1[i] __ word2[j]:
          dp[i + 1][j + 1] = dp[i][j]
        ____:
          dp[i + 1][j + 1] = m..(dp[i][j + 1] + 1, dp[i + 1][j] + 1)
    r.. dp[-1][-1]
