_______ bisect


c_ Solution(o..
  ___ maxSumSubmatrix  matrix, k
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    ans = f__("-inf")
    dp = [[0] * l..(matrix[0]) ___ _ __ r..(l..(matrix))]
    ___ i __ r..(0, l..(matrix)):
      ___ j __ r..(0, l..(matrix[0])):
        dp[i][j] = dp[i][j - 1] + matrix[i][j]
    ___ start __ r..(0, l..(matrix[0])):
      ___ end __ r..(start, l..(matrix[0])):
        sums = [0]
        subsum = 0
        ___ i __ r..(0, l..(matrix)):
          __ start > 0:
            subsum += dp[i][end] - dp[i][start - 1]
          ____:
            subsum += dp[i][end]
          idx = bisect.bisect_left(sums, subsum - k)
          __ idx < l..(sums
            ans = m..(ans, subsum - sums[idx])
          bisect.insort(sums, subsum)
    r.. ans
