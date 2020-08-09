class Solution(object
  ___ minDistance(self, word1, word2
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    dp = [[0] * (le.(word2) + 1) for _ in range(le.(word1) + 1)]
    for i in range(1, le.(word2) + 1
      dp[0][i] = i
    for i in range(1, le.(word1) + 1
      dp[i][0] = i

    for i in range(le.(word1)):
      for j in range(le.(word2)):
        __ word1[i] __ word2[j]:
          dp[i + 1][j + 1] = dp[i][j]
        ____
          dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] + 1)
    r_ dp[-1][-1]
