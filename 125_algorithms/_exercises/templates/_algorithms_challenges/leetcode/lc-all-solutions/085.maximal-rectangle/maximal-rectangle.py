class Solution(object):
  ___ maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    ___ histogram(height):
      __ not height:
        return 0
      height.append(-1)
      stack = []
      ans = 0
      for i in range(0, len(height)):
        while stack and height[i] < height[stack[-1]]:
          h = height[stack.pop()]
          w = i - stack[-1] - 1 __ stack else i
          ans = max(ans, h * w)
        stack.append(i)
      return ans

    ans = 0
    dp = [[0] * len(matrix[0]) for _ in range(0, len(matrix))]
    for i in reversed(range(0, len(matrix))):
      __ i == len(matrix) - 1:
        dp[i] = [int(h) for h in matrix[i]]
      else:
        for j in range(0, len(matrix[0])):
          __ matrix[i][j] != "0":
            dp[i][j] = dp[i + 1][j] + 1
      ans = max(ans, histogram(dp[i]))
    return ans
