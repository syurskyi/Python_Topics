#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Pythonic way.
    ___ searchInsert  nums, target
        r_ l..([x ___ x __ nums __ x < target])


c.. Solution_2 o..
    ___ searchInsert  nums, target
        left, right = 0, l..(nums) - 1
        _____ left <= right:
            mid = (left + right) / 2
            __ target __ nums[mid]:
                r_ mid

            ____ target > nums[mid]:
                left = mid + 1

            ____
                right = mid - 1

        r_ left

"""
[1,3,5,6]
5
[1,3,5,6]
2
[1,3,5,6]
7
[1,3,5,6]
0
"""
