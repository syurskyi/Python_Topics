#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ subsets  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets   # list
        n = l..(nums)
        nums.sort()
        # We know there are totally 2^n subsets,
        # becase every num may in or not in one subsets.
        # So we check the jth(0<=j<n) bit for every ith(0=<i<2^n) subset.
        # If jth bit is 1, then nums[j] in the subset.
        sum_sets = 2 ** n
        ___ i __ r..(sum_sets
            cur_set   # list
            ___ j __ r..(n
                power = 2 ** j
                __ i & power __ power:
                    cur_set.append(nums[j])

            subsets.append(cur_set)

        r_ subsets

"""
[0]
[]
[1,2,3,4,7,8]
"""
