class Solution(object
  ___ maxProfit(self, prices
    """
    :type prices: List[int]
    :rtype: int
    """
    __ not prices:
      r_ 0
    ans = 0
    pre = prices[0]
    ___ i in range(1, le.(prices)):
      pre = min(pre, prices[i])
      ans = max(prices[i] - pre, ans)
    r_ ans
