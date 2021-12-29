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


class Solution:
    ___ hasAlternatingBits(self, n: int) -> bool:
        last = N..
        while n:
            cur = n & 1
            # `if last` is error
            __ last __ n.. N.. and last ^ cur __ 0:
                r.. False
            last = cur
            n >>= 1

        r.. True


__ __name__ __ "__main__":
    ... Solution().hasAlternatingBits(5) __ True
    ... Solution().hasAlternatingBits(7) __ False
