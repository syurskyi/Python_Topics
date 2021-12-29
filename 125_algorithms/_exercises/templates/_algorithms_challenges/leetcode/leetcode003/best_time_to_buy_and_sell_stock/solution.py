"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.
"""


class Solution(object):
    ___ maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        __ n.. prices:
            r.. 0
        max_profit = 0
        min_price = prices[0]
        ___ i, p __ enumerate(prices):
            max_profit = max(max_profit, (p - min_price))
            min_price = m..(min_price, p)
        r.. max_profit
