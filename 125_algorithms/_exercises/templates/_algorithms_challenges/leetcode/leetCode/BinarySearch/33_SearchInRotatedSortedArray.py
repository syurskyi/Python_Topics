#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ search  nums, target
        nums_size = l..(nums)
        start = 0
        end = nums_size - 1
        _____ start <= end:
            mid = (start + end) / 2
            num_mid = nums[mid]

            # Mid is in the left part of the rotated(if it's rotated) array.
            __ num_mid >= nums[start]:
                __ nums[start] <= target < num_mid:
                    end = mid - 1
                ____ num_mid __ target:
                    r_ mid
                ____
                    start = mid + 1

            # The array must be rotated, and mid is in the right part
            ____
                __ num_mid < target <= nums[end]:
                    start = mid + 1
                ____ target __ num_mid:
                    r_ mid
                ____
                    end = mid - 1

        r_ -1

"""
[]
0
[1]
1
[8,11,13,1,3,4,5,7]
7
[4,5,6,7,8,1,2,3]
8
[5, 1, 3]
1
"""
