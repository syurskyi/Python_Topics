"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an
algorithm to find the maximum profit.
"""
__author__ = 'Danyang'


c_ Solution(object):
    ___ maxProfit  A):
        """
        Maximum subarray sum
        DP version
        Let F[i] be the maximum subarray sum ending at A[i-1]
        """
        __ l..(A) <= 1:
            r.. 0

        n = l..(A)
        F = [0 ___ _ __ xrange(n+1)]
        maxa = 0
        ___ i __ xrange(2, n+1):
            F[i] = m..(F[i-1] + A[i-1] - A[i-2], 0)  # revert the previous transaction
            maxa = m..(maxa, F[i])

        r.. maxa

    ___ maxProfitDelta  prices):
        """
        Only long position allowed, cannot short

        Algorithm: max-array problem

        convert to maximum sub-array problem
        two pointer

        :param prices: a list of integer
        :return: integer, max profit
        """
        __ l..(prices) <= 1:
            r.. 0
        delta_prices    # list
        ___ i __ xrange(1, l..(prices)):
            delta_prices.a..(prices[i]-prices[i-1])

        # O(n)
        # notice: possible to do nothing thus profit at least is 0 
        max_sub_array = 0
        current_sub_array = 0
        ___ j __ xrange(l..(delta_prices)):
            current_sub_array = m..(0, current_sub_array+delta_prices[j])
            max_sub_array = m..(max_sub_array, current_sub_array)

        r.. max_sub_array


__ _______ __ _______
    ... Solution().maxProfit([3, 2, 1, 4, 5, 6, 2]) __ 5