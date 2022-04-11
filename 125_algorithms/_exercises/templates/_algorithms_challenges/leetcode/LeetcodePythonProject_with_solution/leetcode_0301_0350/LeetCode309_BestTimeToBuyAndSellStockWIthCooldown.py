
c_ Solution(o..
    ___ maxProfit  prices
        """
        :type prices: List[int]
        :rtype: int
        """
        __ n.. prices: r.. 0
        n l..(prices)
        buy [0]*n
        sell [0]*n
        rest [0]*n
        buy[0] -prices[0]
        ___ i __ r..(1, n
            buy[i] m..(buy[i-1], rest[i-1]-prices[i])
            sell[i] m..(sell[i-1], buy[i-1]+prices[i])
            rest[i] m..(buy[i-1], sell[i-1], rest[i-1])
        r.. m..(buy[-1], sell[-1], rest[-1])
    
    ___ maxProfit1  prices
        n l..(prices)
        __ n < 2: r.. 0
        s0 [0]*n
        s1 [0]*n
        s2 [0]*n
        s1[0] -prices[0]
        s2[0] f__('-inf')
        ___ i __ r..(1, n
            s0[i] m..(s0[i-1], s2[i-1])
            s1[i] m..(s1[i-1], s0[i-1]-prices[i])
            s2[i] s1[i-1] + prices[i]
        r.. m..(s0[-1], s2[-1])
    
    ___ maxProfit2  prices
        n l..(prices)
        __ n < 2: r.. 0
        prev_buy, buy, prev_sell, sell 0, -prices[0], 0, 0
        ___ price __ prices:
            prev_buy buy
            buy m..(prev_sell - price, prev_buy)
            prev_sell sell
            sell m..(prev_buy + price, prev_sell)
        r.. sell
    
    