class Solution(object
  ___ maximalRectangle(self, matrix
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    ___ histogram(height
      __ not height:
        r_ 0
      height.append(-1)
      stack = []
      ans = 0
      ___ i in range(0, le.(height)):
        w___ stack and height[i] < height[stack[-1]]:
          h = height[stack.p..]
          w = i - stack[-1] - 1 __ stack else i
          ans = max(ans, h * w)
        stack.append(i)
      r_ ans

    ans = 0
    dp = [[0] * le.(matrix[0]) ___ _ in range(0, le.(matrix))]
    ___ i in reversed(range(0, le.(matrix))):
      __ i __ le.(matrix) - 1:
        dp[i] = [int(h) ___ h in matrix[i]]
      ____
        ___ j in range(0, le.(matrix[0])):
          __ matrix[i][j] != "0":
            dp[i][j] = dp[i + 1][j] + 1
      ans = max(ans, histogram(dp[i]))
    r_ ans
