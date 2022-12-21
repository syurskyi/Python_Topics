#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-08-23 09:44:33


c.. Solution o..
    """
    If you sum the ith bit of all numbers and mod 3,
    it must be either 0 or 1 due to the constraint of this problem
    where each number must appear either three times or once.
    This will be the ith bit of that "single number".

    Refer to:
    https://discuss.leetcode.com/topic/455/constant-space-solution
    """
    ___ singleNumber  nums
        bit_record = [0] * 32
        result = 0
        ___ i __ r..(32
            ___ n __ nums:
                bit_record[i] += (n >> i) & 0x1
            bit_val = bit_record[i] % 3
            result |= bit_val << i

        # Int in python is an object and has no upper limit,
        # If you do 1<<31, you get 2147483648 other than -2147483648
        r_ result - 2**32 __ result >= 2**31 else result


c.. Solution_2 o..
    """
    Use two-bits represents the sum(should be 0/3, 1, 2) of all num's i-th bit.
    Twice-Once(the two bits): 00(0, 3)-->01(1)-->10(2)-->00(0, 3)
    Then we need to set rules for 'once' and 'twice' so that they act as we hopes.
        once = once ^ n & (~twice)
        twice = twice ^ n & (~once)

    Since each of the 32 bits follow the same rules,
    we can calculate them all at once.  Refer to:
    https://discuss.leetcode.com/topic/2031/challenge-me-thx/17
    """
    ___ singleNumber  nums
        once, twice = 0, 0
        ___ n __ nums:
            once = once ^ n & (~twice)
            twice = twice ^ n & (~once)
        r_ once


"""
[1]
[1,1,3,1]
[1,1,1,2,2,2,3,4,4,4]
[-2,-2,1,1,-3,1,-3,-3,-4,-2]
"""
