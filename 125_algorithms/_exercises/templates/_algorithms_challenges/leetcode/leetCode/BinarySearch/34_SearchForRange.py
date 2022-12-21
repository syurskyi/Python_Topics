#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # log(n) here.
    ___ firstAppear  nums, target
        left, right = 0, l..(nums) - 1
        _____ left <= right:
            mid = (left + right) / 2
            __ target __ nums[mid] and mid - 1 >= left and target __ nums[mid - 1]:
                right = mid - 1
            ____ target __ nums[mid]:
                r_ mid
            ____ target > nums[mid]:
                left = mid + 1
            ____
                right = mid - 1
        r_ -1

    # log(n) again.
    ___ lastAppear(s.., nums, target
        left, right = 0, l..(nums) - 1
        _____ left <= right:
            mid = (left + right) / 2
            __ target __ nums[mid] and mid + 1 <= right and target __ nums[mid + 1]:
                left = mid + 1
            ____ target __ nums[mid]:
                r_ mid
            ____ target > nums[mid]:
                left = mid + 1
            ____
                right = mid - 1
        r_ -1

    ___ searchRange  nums, target
        r_ (self.firstAppear(nums, target), self.lastAppear(nums, target))

"""
[]
0
[1,1,1,1]
1
[1,2,3,4,5]
3
[1,2,3,4,5]
6
"""
