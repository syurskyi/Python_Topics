#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-02 17:09:49


c.. Solution o..
    """
    Firstly, calculate the carry.
    then calculate sum of a and b without thinking the carry.
    Finally add sum(without carry) and carry.
    """
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK = 0x100000000

    ___ getSum  a, b
        __ b __ 0:
            r_ a __ a <= self.MAX_INT else (a % self.MIN_INT) - self.MIN_INT

        add_sum = (a ^ b) % self.MASK
        carry_in = ((a & b) << 1) % self.MASK
        r_ self.getSum(add_sum, carry_in)


c.. Solution_2 o..
    ___ getSum  a, b
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        _____ b != 0:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK

        r_ a __ a <= MAX_INT else (a % MIN_INT) - MIN_INT

"""
0
1
-3
5
12
10000098
-8
-12
"""
