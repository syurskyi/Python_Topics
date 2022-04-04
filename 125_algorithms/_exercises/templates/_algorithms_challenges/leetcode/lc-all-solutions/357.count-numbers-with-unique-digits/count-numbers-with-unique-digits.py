c_ Solution(o..
  ___ countNumbersWithUniqueDigits  n
    """
    :type n: int
    :rtype: int4
    """
    __ n <_ 1:
      r.. 10 ** n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 9
    k = 9
    ___ i __ r..(2, n + 1
      dp[i] = m..(dp[i - 1] * k, 0)
      k -= 1
    r.. s..(dp) + 1
