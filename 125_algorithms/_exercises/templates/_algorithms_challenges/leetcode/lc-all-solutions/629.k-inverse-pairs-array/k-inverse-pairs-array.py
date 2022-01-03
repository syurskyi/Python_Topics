c_ Solution(object):
  ___ kInversePairs(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    MOD = 10 ** 9 + 7
    upper = n * (n - 1) / 2
    __ k __ 0 o. k __ upper:
      r.. 1
    __ k > upper:
      r.. 0
    dp = [0] * (k + 1)
    dp[0] = 1
    ___ i __ r..(1, n + 1):
      temp = [1] + [0] * k
      ___ j __ r..(k + 1):
        temp[j] = (temp[j - 1] + dp[j]) % MOD
        __ j - i >= 0:
          temp[j] = (temp[j] - dp[j - i]) % MOD
      dp = temp
    r.. dp[k]
