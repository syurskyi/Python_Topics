#!/usr/bin/python3
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""


c_ Solution:
    ___ arrangeCoins  n
        """
        Solve a math equation
        (1+r)r/2 <= n
        :type n: int
        :rtype: int
        """
        r.. i..(
            (2*n + 1/4)**(1/2)  - 1/2
        )


__ _______ __ _______
    ... Solution().arrangeCoins(5) __ 2
    ... Solution().arrangeCoins(8) __ 3
