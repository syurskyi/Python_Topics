"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
__author__ = 'Daniel'


c_ Solution:
    ___ maxProfit  k, prices
        """
        DP
        local_{i,j} = \max(global_{i-1.j-1}+\Delta, local_{i-1,j}+\Delta)

        global_{i,j} = \max(local_{i, j}, global_{i-1,j})
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = l..(prices)
        __ k >_ n:
            r.. maxProfit_unlimited_transactions(prices)

        l = [0 ___ _ __ x..(k+1)]  # local max
        g = [0 ___ _ __ x..(k+1)]  # global max
        gmax = 0
        ___ i __ x..(1, n
            diff = prices[i] - prices[i-1]
            ___ j __ x..(k, 0, -1
                l[j] = m..(g[j-1]+diff, l[j]+diff)
                g[j] = m..(l[j], g[j])
                gmax = m..(gmax, g[j])

        r.. gmax

    ___ maxProfit_unlimited_transactions  prices
        profit = 0
        ___ i __ x..(1, l..(prices:
            profit += m..(0, prices[i] - prices[i-1])
        r.. profit

__ _______ __ _______
    print Solution().maxProfit(2, [1, 2, 4])