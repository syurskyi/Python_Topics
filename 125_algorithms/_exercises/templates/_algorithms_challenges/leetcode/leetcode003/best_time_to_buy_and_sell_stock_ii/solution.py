"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the
same time (ie, you must sell the stock before you buy again).
"""


c_ Solution(object):
    ___ maxProfit  prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        __ n.. prices:
            r.. 0
        max_profit = 0
        ___ i __ r..(1, l..(prices)):
            __ prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        r.. max_profit
