#!/usr/bin/python3
"""
Given a non-negative integer N, find the largest number that is less than or
equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair
of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""


c_ Solution:
    ___ monotoneIncreasingDigits(self, N: i..) __ i..:
        """
        332
        322
        222
        fill 9
        299
        """
        d.. = [i..(e) ___ e __ s..(N)]
        pointer = l..(d..)
        ___ i __ r..(l..(d..) - 1, 0, -1):
            __ d..[i - 1] > d..[i]:
                pointer = i
                d..[i - 1] -= 1

        ___ i __ r..(pointer, l..(d..)):
            d..[i] = 9

        r.. i..("".j..(map(s.., d..)))


__ _______ __ _______
    ... Solution().monotoneIncreasingDigits(10) __ 9
    ... Solution().monotoneIncreasingDigits(332) __ 299
