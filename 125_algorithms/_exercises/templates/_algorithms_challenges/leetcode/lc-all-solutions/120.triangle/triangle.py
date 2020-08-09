class Solution(object
  ___ minimumTotal(self, triangle
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = [0] * le.(triangle)
    dp[0] = triangle[0][0]
    ___ i in range(1, le.(triangle)):
      pre = dp[0]
      ___ j in range(le.(triangle[i])):
        tmp = dp[j]
        __ j __ 0:
          dp[j] = pre
        ____ j __ le.(triangle[i]) - 1:
          dp[j] = pre
        ____
          dp[j] = min(dp[j], pre)
        dp[j] += triangle[i][j]
        pre = tmp
    r_ min(dp)
