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
    for i in range(2, n + 1
      dp[i] = max(dp[i - 1] * k, 0)
      k -= 1
    r_ sum(dp) + 1
