#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ subsetsWithDup  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        __ n.. nums:
            r_ []

        nums.s.. )
        nums_len = l..(nums)

        # Keep the subsets without duplicate subsets
        subsets = [[nums[0]]]
        # Keep the previous subsets which contains previous nums.
        pre_subset = [[nums[0]]]

        ___ i __ r..(1, nums_len
            # Combine current num with the previous subsets,
            # Then update the previous subsets
            __ nums[i] __ nums[i-1]:
                ___ j __ r..(l..(pre_subset)):
                    one_set = pre_subset[j][:]
                    one_set.a.. nums[i])
                    subsets.a.. one_set)
                    pre_subset[j] = one_set

            # Combine current num with all the subsets before.
            # Then update the previous subsets
            ____
                pre_subset   # list
                ___ j __ r..(l..(subsets)):
                    one_set = subsets[j][:]
                    one_set.a.. nums[i])
                    subsets.a.. one_set)
                    pre_subset.a.. one_set)
                pre_subset.a.. [nums[i]])
                subsets.a.. [nums[i]])

        subsets.a.. [])
        r_ subsets

"""
[]
[1,2]
[1,2,2]
[1,2,2,3,3,4,5]
"""
