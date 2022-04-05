c_ Solution(o..
  ___ generateMatrix  n
    """
    :type n: int
    :rtype: List[List[int]]
    """
    ans = [[0] * n ___ _ __ r..(n)]
    left, right, up, down = 0, n - 1, 0, n - 1
    k = 1
    w.... left <_ right a.. up <_ down:
      ___ i __ r..(left, right + 1
        ans[up][i] = k
        k += 1
      up += 1
      ___ i __ r..(up, down + 1
        ans[i][right] = k
        k += 1
      right -_ 1
      ___ i __ r..(r..(left, right + 1:
        ans[down][i] = k
        k += 1
      down -_ 1
      ___ i __ r..(r..(up, down + 1:
        ans[i][left] = k
        k += 1
      left += 1
    r.. ans
