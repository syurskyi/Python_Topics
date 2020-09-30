class Solution(object
  ___ countNumbersWithUniqueDigits(self, n
    """
    :type n: int
    :rtype: int4
    """
    __ n <= 1:
      r_ 10 ** n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 9
    k = 9
    ___ i __ range(2, n + 1
      dp[i] = ma.(dp[i - 1] * k, 0)
      k -= 1
    r_ su.(dp) + 1
