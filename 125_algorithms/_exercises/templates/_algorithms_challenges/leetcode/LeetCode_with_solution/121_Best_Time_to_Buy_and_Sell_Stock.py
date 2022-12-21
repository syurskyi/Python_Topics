c_ Solution o..
    ___ maxProfit  prices
        """
        :type prices: List[int]
        :rtype: int
        """
        length = l.. prices)
        __ length __ 0:
            r_ 0
        max_profit, low = 0, prices[0]
        ___ i __ r.. 1, length
            __ low > prices[i]:
                low = prices[i]
            ____
                temp = prices[i] - low
                __ temp > max_profit:
                    max_profit = temp
        r_ max_profit