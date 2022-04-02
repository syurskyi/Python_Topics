c_ Solution(o..
  ___ maximalRectangle  matrix
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    ___ histogram(height
      __ n.. height:
        r.. 0
      height.a..(-1)
      stack    # list
      ans = 0
      ___ i __ r..(0, l..(height)):
        w.... stack a.. height[i] < height[stack[-1]]:
          h = height[stack.pop()]
          w = i - stack[-1] - 1 __ stack ____ i
          ans = m..(ans, h * w)
        stack.a..(i)
      r.. ans

    ans = 0
    dp = [[0] * l..(matrix[0]) ___ _ __ r..(0, l..(matrix))]
    ___ i __ r..(r..(0, l..(matrix))):
      __ i __ l..(matrix) - 1:
        dp[i] = [i..(h) ___ h __ matrix[i]]
      ____:
        ___ j __ r..(0, l..(matrix[0])):
          __ matrix[i][j] != "0":
            dp[i][j] = dp[i + 1][j] + 1
      ans = m..(ans, histogram(dp[i]))
    r.. ans
