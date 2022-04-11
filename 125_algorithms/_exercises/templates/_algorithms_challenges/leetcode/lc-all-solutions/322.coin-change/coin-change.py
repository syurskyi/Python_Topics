c_ Solution(o..
  ___ coinChange  coins, amount
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    dp [f__("inf")] * (amount + 1)
    dp[0] 0
    ___ i __ r..(1, amount + 1
      ___ coin __ coins:
        __ i - coin >_ 0:
          dp[i] m..(dp[i], dp[i - coin] + 1)
    r.. dp[-1] __ dp[-1] != f__("inf") ____ -1
