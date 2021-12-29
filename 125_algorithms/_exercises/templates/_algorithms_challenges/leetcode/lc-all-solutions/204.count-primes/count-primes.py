class Solution(object):

  ___ countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """

    ___ helper(n, dp):
      for i in range(2, n):
        __ dp[i] == 1:
          k = i * i
          __ k >= n:
            return
          while k < n:
            dp[k] = 0
            k += i

    __ n < 2:
      return 0
    ans = 0
    dp = [1] * n
    dp[0] = 0
    dp[1] = 0
    helper(n, dp)
    # for i in range(0, n):
    #     if dp[i] == 1:
    #         print i + 1

    return sum(dp)
