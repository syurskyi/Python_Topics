"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you
must sell the stock before you buy again).
"""
__author__ = 'Danyang'


c_ Solution:
    ___ maxProfit  prices):
        """
        multiple transactions
        you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

        Algorithm: transformed array

        :param prices: list of integers
        :return: integer
        """
        __ l..(prices) <= 1:
            r.. 0

        delta_prices    # list  # \delta
        ___ i __ xrange(1, l..(prices)):
            delta_prices.a..(prices[i]-prices[i-1])

        # O(n)
        profit = 0
        ___ i __ xrange(l..(delta_prices)):
            __ delta_prices[i] > 0:
                profit += delta_prices[i]

        r.. profit