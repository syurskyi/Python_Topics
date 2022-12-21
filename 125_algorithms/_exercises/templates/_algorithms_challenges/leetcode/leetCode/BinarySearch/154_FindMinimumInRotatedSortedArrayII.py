#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ findMin  nums
        assert(nums)
        left = 0
        right = l..(nums) - 1
        # Make sure right is always in the right rotated part.
        # Left can be either in the left part or the minimum part.
        # So, when left and right is the same finally, we find the minimum.
        _____ left < right:
            # When there is no rotate, just return self.nums[start]
            __ nums[left] < nums[right]:
                r_ nums[left]

            mid = (left + right) / 2
            # mid is in the left part, so move the left point to mid.
            __ nums[left] < nums[mid]:
                left = mid + 1
            ____ nums[left] > nums[mid]:
                right = mid
            # Can't make sure whether left is in the left part or not.
            # Just move to right for 1 step.
            ____
                left += 1
        r_ nums[left]

"""
[1]
[7,8,9,9,9,10,2,2,2,3,4,4,5]
"""
