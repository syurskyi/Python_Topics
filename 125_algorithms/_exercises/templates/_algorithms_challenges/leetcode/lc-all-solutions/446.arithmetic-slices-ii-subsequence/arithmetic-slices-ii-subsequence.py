c_ Solution(o..
  ___ numberOfArithmeticSlices  A
    """
    :type A: List[int]
    :rtype: int
    """
    ans = 0
    dp = [c...d..(i..) ___ _ __ A]
    ___ i __ r..(l..(A)):
      ___ j __ r..(i
        diff = A[i] - A[j]
        dp[i][diff] += 1
        __ diff __ dp[j]:
          dp[i][diff] += dp[j][diff]
          ans += dp[j][diff]
    r.. ans
