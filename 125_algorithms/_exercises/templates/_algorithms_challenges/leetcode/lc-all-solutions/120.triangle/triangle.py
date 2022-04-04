c_ Solution(o..
  ___ minimumTotal  triangle
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    dp = [0] * l..(triangle)
    dp[0] = triangle[0][0]
    ___ i __ r..(1, l..(triangle:
      pre = dp[0]
      ___ j __ r..(l..(triangle[i]:
        tmp = dp[j]
        __ j __ 0:
          dp[j] = pre
        ____ j __ l..(triangle[i]) - 1:
          dp[j] = pre
        ____:
          dp[j] = m..(dp[j], pre)
        dp[j] += triangle[i][j]
        pre = tmp
    r.. m..(dp)
