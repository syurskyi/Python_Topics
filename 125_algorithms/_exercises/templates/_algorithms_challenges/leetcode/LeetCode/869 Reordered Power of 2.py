#!/usr/bin/python3
"""
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
"""
from collections ______ Counter


class Solution:
    ___ reorderedPowerOf2(self, N: int) -> bool:
        """
        count the digit and compare
        """
        counts = Counter(str(N))
        ___ i in range(31  # 32 bit unsighed int
            __ counts __ Counter(str(1 << i)):
                r_ True
        ____
            r_ False
