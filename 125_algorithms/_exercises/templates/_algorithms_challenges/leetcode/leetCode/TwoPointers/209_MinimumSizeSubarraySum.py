#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Maintain a minimum window with  two indices.
    ___ minSubArrayLen  s, nums
        __ n.. nums:
            r_ 0
        start, end, sums, min_len = 0, 0, nums[0], 0
        len_nums = l..(nums)
        _____ end < len_nums:
            __ sums < s a.. end + 1 < len_nums:
                end += 1
                sums += nums[end]
            __ sums >= s:
                __ min_len __ 0:
                    min_len = end - start + 1
                ____
                    min_len = min(min_len, end - start + 1)
                sums -= nums[start]
                __ start < end:
                    start += 1
            __ end __ len_nums - 1 a.. sums < s:
                ______
        r_ min_len

"""
100
[]
20
[1,3,12,8,3,4,21]
0
[1,1,2]
4
[1,4,4]
"""
