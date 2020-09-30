"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
__author__ = 'Daniel'


class Solution:
    ___ maxProfit(self, k, prices
        """
        DP
        local_{i,j} = \max(global_{i-1.j-1}+\Delta, local_{i-1,j}+\Delta)

        global_{i,j} = \max(local_{i, j}, global_{i-1,j})
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = le.(prices)
        __ k >= n:
            r_ self.maxProfit_unlimited_transactions(prices)

        l = [0 ___ _ __ xrange(k+1)]  # local max
        g = [0 ___ _ __ xrange(k+1)]  # global max
        gmax = 0
        ___ i __ xrange(1, n
            diff = prices[i] - prices[i-1]
            ___ j __ xrange(k, 0, -1
                l[j] = ma.(g[j-1]+diff, l[j]+diff)
                g[j] = ma.(l[j], g[j])
                gmax = ma.(gmax, g[j])

        r_ gmax

    ___ maxProfit_unlimited_transactions(self, prices
        profit = 0
        ___ i __ xrange(1, le.(prices)):
            profit += ma.(0, prices[i] - prices[i-1])
        r_ profit

__  -n __ "__main__":
    print Solution().maxProfit(2, [1, 2, 4])