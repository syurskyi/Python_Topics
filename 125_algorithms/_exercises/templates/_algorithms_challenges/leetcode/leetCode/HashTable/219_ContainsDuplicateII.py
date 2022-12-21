#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ containsNearbyDuplicate  nums, k
        hash_dict _ # dict
        __ n.. nums:
            r_ False
        len_nums = l..(nums)
        ___ i __ r..(len_nums
            num = nums[i]
            __ num __ hash_dict a.. i - hash_dict[num] <= k:
                r_ True
            hash_dict[num] = i
        r_ False

"""
[]
3
[1,2,3,3]
1
[1,2,3,4,1]
3
"""
