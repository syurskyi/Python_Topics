#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ summaryRanges  nums
        nums.a.. "#")      # Guard
        range_str   # list
        start, end = nums[0], nums[0]
        ___ i __ xrange(1, l..(nums)):
            __ nums[i] __ nums[i-1] + 1:
                end += 1
            ____
                __ start __ end:
                    range_str.a.. str(start))
                ____
                    range_str.a.. str(start) + "->" + str(end))
                start = end = nums[i]
        r_ range_str

"""
[]
[-1]
[0,1,2,3,5,8,9,11]
"""
