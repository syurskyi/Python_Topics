#!/usr/bin/python3
"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.
"""


class Solution:
    ___ hammingDistance(self, x, y
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x ^ y
        ret = 0
        w___ diff:
            ret += diff & 1
            diff >>= 1
            
        r_ ret


__ __name__ __ "__main__":
    assert Solution().hammingDistance(3, 1) __ 1
    assert Solution().hammingDistance(1, 4) __ 2
