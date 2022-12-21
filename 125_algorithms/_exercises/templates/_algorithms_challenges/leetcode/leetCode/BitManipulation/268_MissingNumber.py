#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # XOR all the num in nums and sequence from 0 to n,
    # All the num in nums occur twice, then the result is the missing one
    ___ missingNumber  nums
        i = 0
        missing_num = 0
        ___ num __ nums:
            missing_num ^= num
            missing_num ^= i
            i += 1
        missing_num ^= i
        r_ missing_num

"""
[0]
[1]
[1,2,3]
[0,1,2,3,5,7,8,6]
"""
