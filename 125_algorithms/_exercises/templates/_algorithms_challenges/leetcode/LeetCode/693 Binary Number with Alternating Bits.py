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
        last = None
        w___ n:
            cur = n & 1
            # `if last` is error
            __ last pa__ not None and last ^ cur __ 0:
                r_ False
            last = cur
            n >>= 1

        r_ True


__  -n __ "__main__":
    assert Solution().hasAlternatingBits(5) __ True
    assert Solution().hasAlternatingBits(7) __ False
