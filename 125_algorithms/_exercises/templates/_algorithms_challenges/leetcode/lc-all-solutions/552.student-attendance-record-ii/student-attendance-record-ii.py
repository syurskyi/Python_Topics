c_ Solution(o..
  ___ checkRecord  n
    """
    :type n: int
    :rtype: int
    """
    M = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[:3] = [1, 2, 4]

    ___ i __ r..(3, n + 1
      dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % M
    ans = dp[n]

    ___ i __ r..(1, n + 1
      ans += (dp[i - 1] * dp[n - i]) % M
      ans %= M
    r.. ans % M
