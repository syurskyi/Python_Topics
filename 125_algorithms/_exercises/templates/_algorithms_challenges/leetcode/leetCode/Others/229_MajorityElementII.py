#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# According to:
# https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration


c.. Solution o..
    ___ majorityElement  nums
        __ n.. nums:
            r_ []
        candidate_1, candidate_2 = 0, 1
        count_1, count_2 = 0, 0
        ___ num __ nums:
            __ num __ candidate_1:
                count_1 += 1
            ____ num __ candidate_2:
                count_2 += 1
            ____ n.. count_1:
                candidate_1, count_1 = num, 1
            ____ n.. count_2:
                candidate_2, count_2 = num, 1
            ____
                count_1 -= 1
                count_2 -= 1
        result   # list
        ___ num __ [candidate_1, candidate_2]:
            __ nums.c..(num) > l..(nums) / 3:
                result.a.. num)
        r_ result
"""
[]
[0,0,0]
[1,2,2,3,3,1,1,1]
[2,2,2,3,3,4,3,2]
[1,1,2]
[3,0,3,4]
"""
