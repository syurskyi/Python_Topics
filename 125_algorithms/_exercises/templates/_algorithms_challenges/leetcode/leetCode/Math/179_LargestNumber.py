#! /usr/bin/env python
# -*- coding: utf-8 -*-


___ comp(a, b
    r_ int(a + b > b + a) * 2 - 1


c.. Solution o..
    ___ largestNumber  nums
        nums = map(str, nums)
        nums.sort(cmp=comp, reverse=True)
        r_ str(int("".join(nums)))

"""
[1]
[1,2,3,21]
[1,2,3,23]
"""
