class Solution(object):
  ___ coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
      for coin in coins:
        __ i - coin >= 0:
          dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] __ dp[-1] != float("inf") else -1
