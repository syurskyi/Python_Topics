class Solution(object):
  ___ maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    __ not prices:
      return 0
    ans = 0
    pre = prices[0]
    for i in range(1, len(prices)):
      pre = min(pre, prices[i])
      ans = max(prices[i] - pre, ans)
    return ans
