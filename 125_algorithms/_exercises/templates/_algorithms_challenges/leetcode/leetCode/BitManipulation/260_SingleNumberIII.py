#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Clear explanation according to
    # https://leetcode.com/discuss/60408/sharing-explanation-of-the-solution
    ___ singleNumber  nums
        xor_res = 0
        ___ num __ nums:
            xor_res ^= num

        # Assume the two different numbers diff at ith bit(i is the rightmost).
        # Then we can get 0x000...1...000, 1 is the ith bit by the following.
        xor_res &= -xor_res
        num_a, num_b = 0, 0
        ___ num __ nums:
            # All the numbers can be partitioned into
            # two groups according to their bits at location i.
            # The first group consists of all numbers whose bits at i is 0.
            # The second group consists of all numbers whose bits at i is 1.
            # The two different number a and b is in the two different groups.
            __ num & xor_res __ 0:
                num_a ^= num
            ____
                num_b ^= num
        r_ [num_a, num_b]

"""
[-1,0]
[1, 2, 1, 3, 2, 5]
[-1,-1,-2,-2,-3,-3,-3,-3,4,-5]
"""
