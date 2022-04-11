#!/usr/bin/python3
"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.
"""


c_ Solution:
    ___ hammingDistance  x, y
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff x ^ y
        ret 0
        w.... diff:
            ret += diff & 1
            diff >>= 1
            
        r.. ret


__ _______ __ _______
    ... Solution().hammingDistance(3, 1) __ 1
    ... Solution().hammingDistance(1, 4) __ 2
