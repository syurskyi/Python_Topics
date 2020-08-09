class Solution(object
  ___ maxProfit(self, prices
    """
    :type prices: List[int]
    :rtype: int
    """
    ans = 0
    ___ i in range(1, le.(prices)):
      __ prices[i] > prices[i - 1]:
        ans += prices[i] - prices[i - 1]
    r_ ans
