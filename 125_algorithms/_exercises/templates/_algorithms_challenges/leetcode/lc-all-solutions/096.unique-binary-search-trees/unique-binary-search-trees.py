c_ Solution(object):
  ___ _numTrees  n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    ___ i __ r..(2, n + 1):
      ___ j __ r..(1, i + 1):
        dp[i] += dp[j - 1] * dp[i - j]
    r.. dp[-1]

  ___ numTrees  n):
    ans = 1
    ___ i __ r..(1, n + 1):
      ans = ans * (n + i) / i
    r.. ans / (n + 1)
