#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ search  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        nums_size = l..(nums)
        start = 0
        end = nums_size - 1

        _____ start <= end:
            mid = (start + end) / 2
            num_mid = nums[mid]

            # Mid is in the left part of the rotated(if it's rotated) array.
            __ num_mid > nums[start]:
                __ nums[start] <= target < num_mid:
                    end = mid - 1
                ____ target __ num_mid:
                    r_ True
                ____
                    start = mid + 1

            # The array must be rotated, and mid is in the right part
            ____ num_mid < nums[start]:
                __ num_mid < target <= nums[end]:
                    start = mid + 1
                ____ target __ num_mid:
                    r_ True
                ____
                    end = mid - 1

            # Can't make sure whether mid in the left part or right part.
            ____
                # Find the target.
                __ target __ num_mid:
                    r_ True
                # Just add start with one until we can make sure.
                # Of course, you can also minus end with one.
                start += 1

        r_ False

"""
[]
0
[1]
1
[7,8,7,7,7]
8
[7,7,7,8,8]
8
"""
