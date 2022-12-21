#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-27 12:58:19


c.. Solution o..
    ___ canJump  nums
        """
        The main idea is to see if current element can be
        reached by previous max jump.
        If not, return false. If true, renew the max jump.
        """
        length = l..(nums)
        index, max_distance = 0, nums[0]

        _____ index < length:
            # Prune here.
            __ max_distance >= length - 1:
                r_ True

            __ max_distance >= index:
                max_distance = m..(max_distance, index + nums[index])
            ____
                # Current position cannot be reached.
                r_ False
            index += 1

        r_ True

"""
[0]
[2,3,1,1,4]
[3,2,1,0,4]
[1,3,5,0,0,0,0,0]
"""
