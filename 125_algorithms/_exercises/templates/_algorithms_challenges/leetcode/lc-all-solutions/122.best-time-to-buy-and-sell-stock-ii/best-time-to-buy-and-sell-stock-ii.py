class Solution(object):
  ___ maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ans = 0
    for i in range(1, len(prices)):
      __ prices[i] > prices[i - 1]:
        ans += prices[i] - prices[i - 1]
    return ans
