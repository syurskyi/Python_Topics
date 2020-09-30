class Solution(object
  ___ maximalSquare(self, matrix
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    __ le.(matrix) __ 0:
      r_ 0
    dp = [[0] * le.(matrix[0]) ___ i __ range(0, le.(matrix))]
    ans = 0
    ___ i __ range(0, le.(matrix)):
      ___ j __ range(0, le.(matrix[0])):
        __ matrix[i][j] __ "1":
          __ i __ 0:
            dp[i][j] = 1
          ____ j __ 0:
            dp[i][j] = 1
          ____
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
          ans = ma.(ans, dp[i][j])
    r_ ans * ans
