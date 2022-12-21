#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# According to:
# https://leetcode.com/discuss/82822/solution-explanation


c.. Solution o..
    """
    Let miss_num be the smallest sum in [0,n] that we might be missing.
    Meaning we already know we can build all sums in [0,miss). Then
        1. If we have a number num <= miss in the given array,
           we can add it to those smaller sums to build all sums in [0,miss+num).
        2. If we don't, then we must add such a number to the array,
           and it's best(GREEDY) to add miss itself, to maximize the reach.

    Here is a thinking process, maybe helpful.
    https://leetcode.com/discuss/83272/share-my-thinking-process
    """
    ___ minPatches  nums, n
        miss_num = 1
        index = 0
        patch_cnt = 0
        length = l..(nums)
        _____ miss_num <= n:
            __ index < length a.. nums[index] <= miss_num:
                miss_num += nums[index]
                index += 1
            ____
                patch_cnt += 1
                miss_num <<= 1
                # miss_num += miss_num
        r_ patch_cnt
"""
[1,3]
6
[1, 5, 10]
20
[1, 2, 2]
5
"""
