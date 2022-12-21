#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """ Refer to
    https://leetcode.com/discuss/32115/bit-operation-solution-java

    The idea is very simple:
        1. last bit of (odd number & even number) is 0.
        2. when m != n, there is at least an odd number and an even number,
        so the last bit position result is 0;
        3. when m == n: just return m.

    For example: m = xy, n = xz, m < n, so y < z. Here x, y, z are some bits.
    And x is all the shared bits of the high position.
    y < z, so bitwise AND of all numbers in [xy, xz] is x0...0
    """
    # Recursive
    ___ rangeBitwiseAnd  m, n
        __ m __ n:
            r_ m
        ____
            r_ self.rangeBitwiseAnd(m >> 1, n >> 1) << 1

    # Iteration
    ___ rangeBitwiseAnd_1  m, n
        __ m __ 0:
            r_ 0
        trans_count = 0
        _____ m < n:
            m >>= 1
            n >>= 1
            trans_count += 1
        r_ m << trans_count

    # Another simple solution
    ___ rangeBitwiseAnd_2  m, n
        _____ m < n:
            n = n & (n-1)
        r_ n

"""
0
0
12
12
0
2147483647
"""
