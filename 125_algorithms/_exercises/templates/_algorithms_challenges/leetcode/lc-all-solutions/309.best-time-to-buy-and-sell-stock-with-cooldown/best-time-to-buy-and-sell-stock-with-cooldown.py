c_ Solution(o..
  ___ maxProfit  prices
    """
    :type prices: List[int]
    :rtype: int
    """
    __ l..(prices) < 2:
      r.. 0
    buy = [0] * l..(prices)
    sell = [0] * l..(prices)
    buy[0] = -prices[0]
    buy[1] = m..(-prices[1], buy[0])
    sell[0] = 0
    sell[1] = m..(prices[1] - prices[0], 0)
    ___ i __ r..(2, l..(prices)):
      buy[i] = m..(sell[i - 2] - prices[i], buy[i - 1])
      sell[i] = m..(prices[i] + buy[i - 1], sell[i - 1])
    r.. m..(sell)
