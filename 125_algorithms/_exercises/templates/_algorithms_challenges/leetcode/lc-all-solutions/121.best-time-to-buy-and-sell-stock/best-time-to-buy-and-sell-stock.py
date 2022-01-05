c_ Solution(o..):
  ___ maxProfit  prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    __ n.. prices:
      r.. 0
    ans = 0
    pre = prices[0]
    ___ i __ r..(1, l..(prices)):
      pre = m..(pre, prices[i])
      ans = m..(prices[i] - pre, ans)
    r.. ans
