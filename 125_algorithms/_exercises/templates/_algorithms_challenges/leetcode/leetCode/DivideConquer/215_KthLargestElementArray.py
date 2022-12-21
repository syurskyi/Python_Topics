#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Simple way: O(nlogn)
    ___ findKthLargest  nums, k
        r_ s..(nums)[-k]


c.. Solution_2 o..
    # QuickSelect, according to:
    # http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
    # Heap implement by c++ can be found in c++ version.
    ___ findKthLargest  nums, k
        pivot = nums[0]
        nums1, nums2   # list, []
        ___ num __ nums:
            __ num > pivot:
                nums1.append(num)
            ____ num < pivot:
                nums2.append(num)
        __ k <= l..(nums1
            r_ self.findKthLargest(nums1, k)
        ____ k > l..(nums) - l..(nums2
            r_ self.findKthLargest(nums2, k - (l..(nums) - l..(nums2)))
        ____
            r_ pivot

"""
[1]
1
[3,2,1,5,6,4]
2
[1,2,1,3,9]
2
"""
