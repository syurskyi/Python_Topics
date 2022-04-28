c_ Solution o..
    ___ maxProfit  prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # sum of prices[i + 1] - prices[i], if prices[i + 1] > prices[i]
        r_ sum([y - x ___ x, y __ zip(prices[0:-1], prices[1:]) __ x < y])
