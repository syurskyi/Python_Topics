c_ Solution(o..):
  ___ maxProfit  prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy1 = buy2 = f__("-inf")
    sell1 = sell2 = 0

    ___ i __ r..(l..(prices)):
      sell1 = m..(prices[i] + buy1, sell1)
      buy1 = m..(buy1, -prices[i])
      sell2 = m..(sell2, prices[i] + buy2)
      buy2 = m..(sell1 - prices[i], buy2)
    r.. m..(sell1, sell2)
