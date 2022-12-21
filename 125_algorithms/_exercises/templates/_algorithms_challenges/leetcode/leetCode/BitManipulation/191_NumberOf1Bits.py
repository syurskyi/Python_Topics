#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # pythonic
    ___ hammingWeight  n
        bit_list = list('{0:032b}'.f..(n))
        count = 0
        ___ bit __ bit_list:
            count += int(bit)
        r_ count

    # Bit manipulation
    ___ hammingWeight_1  n
        count = 0
        ___ i __ r..(32
            count += (n >> i) & 1
        r_ count

"""
if __name__ == '__main__':
    sol = Solution()
    print sol.hammingWeight(11)
    print sol.hammingWeight_1(11)
"""
