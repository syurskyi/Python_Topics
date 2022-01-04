#!/usr/bin/python3
"""
Given a positive integer, check whether it has alternating bits: namely, if two
adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
"""


c_ Solution:
    ___ hasAlternatingBits(self, n: i..) __ bool:
        last = N..
        w.... n:
            cur = n & 1
            # `if last` is error
            __ last __ n.. N.. a.. last ^ cur __ 0:
                r.. F..
            last = cur
            n >>= 1

        r.. T..


__ _______ __ _______
    ... Solution().hasAlternatingBits(5) __ T..
    ... Solution().hasAlternatingBits(7) __ F..
