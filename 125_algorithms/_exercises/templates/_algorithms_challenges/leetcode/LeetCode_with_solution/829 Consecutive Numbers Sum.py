#!/usr/bin/python3
"""
Given a positive integer N, how many ways can we write it as a sum of consecutive
positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""


c_ Solution:
    ___ consecutiveNumbersSum  N: i..) __ i..:
        """
        Arithmetic Array
        math

        (x0 + xn) * (xn - x0 + 1) / 2 = N
        xn = x0 + k - 1
        (2x0 + k - 1) * k / 2 = N
        2x0 = 2N / k - k + 1

        x0 * k = N - k * (k - 1) / 2
        # assure for divisibility
        """
        cnt 0
        k 0
        w... T...
            k += 1
            x0k N - k * (k - 1) // 2
            __ x0k <_ 0 :
                _____
            __ x0k % k __ 0:
                cnt += 1

        r.. cnt

    ___ consecutiveNumbersSum_error  N: i..) __ i..:
        """
        Arithmetic Array
        math

        (x0 + xn) * (xn - x0 + 1) / 2 = N
        xn = x0 + k - 1
        (2x0 + k - 1) * k / 2 = N
        2x0 = 2N / k - k + 1

        x0 * k = N - k * (k - 1) / 2
        # assure for divisibility
        """
        cnt 0
        ___ k __ r..(1, i..(N ** 0.5:  # error
            x0k N - k * (k - 1) // 2
            __ x0k % k __ 0:
                cnt += 1

        r.. cnt

    ___ consecutiveNumbersSum_error  N: i..) __ i..:
        """
        factor related
        9 / 3 = 3
        """
        __ N __ 1:
            r.. 1

        cnt 0
        ___ i __ r..(1, N
            d N // i
            r N % i
            __ r __ 0 a.. d - i // 2 > 0
                cnt += 1
            ____ r __ 1 a.. N __ (d + d + 1) * i // 2:
                cnt += 1
        r.. cnt
