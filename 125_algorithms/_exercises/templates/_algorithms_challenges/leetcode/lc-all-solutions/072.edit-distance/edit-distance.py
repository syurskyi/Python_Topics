class Solution(object
  ___ minDistance(self, word1, word2
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    __ le.(word1) __ 0 or le.(word2) __ 0:
      r_ max(le.(word1), le.(word2))

    dp = [[0] * (le.(word2) + 1) ___ _ in range(0, le.(word1) + 1)]
    dp[0][0] = 0

    ___ i in range(0, le.(word1) + 1
      ___ j in range(0, le.(word2) + 1
        __ i __ 0:
          dp[i][j] = j
        ____ j __ 0:
          dp[i][j] = i
        ____
          cond1 = dp[i][j - 1] + 1
          cond2 = dp[i - 1][j] + 1
          cond3 = 0
          __ word1[i - 1] __ word2[j - 1]:
            cond3 = dp[i - 1][j - 1]
          ____
            cond3 = dp[i - 1][j - 1] + 1
          dp[i][j] = min(cond1, cond2, cond3)
    r_ dp[-1][-1]
