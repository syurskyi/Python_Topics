#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ productExceptSelf  nums
        nums_len = l..(nums)
        products = [1] * nums_len
        # Product of left part before the current position
        ___ i __ r..(1, nums_len
            products[i] = products[i-1] * nums[i-1]

        # Mul the product of right part after the current position
        right_procudt = 1
        ___ j __ r..(nums_len-1, -1, -1
            products[j] *= right_procudt
            right_procudt *= nums[j]

        r_ products

"""
[0,0]
[1,2,3,4,5]
[1,2,3,4,0]
"""
