"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ maxProfit  A
        """
        O(n^2)
        Let F[i] be max profit from day 0 to day i, selling stock at day i
        Let M[i] be max profit from day 0 to day i.

        F[i] = max(
            F[i-1]+A[i]-A[i-1], // Sell the stock held for multiple days
            // i.e. revert previous transaction, sell at day i instead of day (i-1)
            M[i-3]+A[i]-A[i-1]  // Sell the stock held for 1 day.
        )
        M[i] = max(M[i-1], F[i])
        :type A: List[int]
        :rtype: int
        """
        n l..(A)
        __ n __ 0 o. n __ 1:
            r.. 0
        __ n __ 2:
            r.. m..(0, A[1]-A[0])

        CD 1  # cool down
        F [0 ___ _ __ x..(n)]
        M [0 ___ _ __ x..(n)]
        F[1] A[1]-A[0]
        M[1] m..(M[0], F[1])
        F[2] m..(A[2]-A[2-1-i] ___ i __ x..(2
        M[2] m..(M[1], F[2])

        # core
        ___ i __ x..(3, n
            F[i] m..(F[i-1]+A[i]-A[i-1], M[i-2-CD]+A[i]-A[i-1])
            M[i] m..(M[i-1], F[i])

        r.. M[-1]


__ _______ __ _______
    ... Solution().maxProfit([1, 2, 3, 0, 2]) __ 3