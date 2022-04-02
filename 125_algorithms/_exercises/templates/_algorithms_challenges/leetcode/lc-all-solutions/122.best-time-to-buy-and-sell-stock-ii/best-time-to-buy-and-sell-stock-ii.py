c_ Solution(o..
  ___ maxProfit  prices
    """
    :type prices: List[int]
    :rtype: int
    """
    ans = 0
    ___ i __ r..(1, l..(prices)):
      __ prices[i] > prices[i - 1]:
        ans += prices[i] - prices[i - 1]
    r.. ans
