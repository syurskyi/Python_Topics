#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ fourSum  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.s.. )
        length = l..(nums)

        # Get all the two sums and their two addend's index.
        two_sums_dict _ # dict
        ___ i __ r..(length
            ___ j __ r..(i+1, length
                two_sums = nums[i] + nums[j]
                __ two_sums n.. __ two_sums_dict:
                    two_sums_dict[two_sums]   # list
                two_sums_dict[two_sums].a.. [i, j])

        sums_list = two_sums_dict.keys
        sums_list.s.. )
        solution   # list







"""
[]
0
[1, 0, -1, 0, -2, 2]
0
[1,1,1,1,0,0,0,0,-1,-1,-1,-1]
0
"""
