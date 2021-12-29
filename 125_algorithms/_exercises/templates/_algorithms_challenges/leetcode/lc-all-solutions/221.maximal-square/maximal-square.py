class Solution(object):
  ___ maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    __ len(matrix) == 0:
      return 0
    dp = [[0] * len(matrix[0]) for i in range(0, len(matrix))]
    ans = 0
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[0])):
        __ matrix[i][j] == "1":
          __ i == 0:
            dp[i][j] = 1
          elif j == 0:
            dp[i][j] = 1
          else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
          ans = max(ans, dp[i][j])
    return ans * ans
