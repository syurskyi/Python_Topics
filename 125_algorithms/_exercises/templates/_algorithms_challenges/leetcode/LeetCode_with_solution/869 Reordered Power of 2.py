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
____ collections _______ Counter


c_ Solution:
    ___ reorderedPowerOf2(self, N: i..) __ bool:
        """
        count the digit and compare
        """
        counts = Counter(s..(N))
        ___ i __ r..(31):  # 32 bit unsighed int
            __ counts __ Counter(s..(1 << i)):
                r.. T..
        ____:
            r.. F..
