#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ sortColors  nums
        len_n = l..(nums)
        # pos_put_0: next position to put 0
        # pos_put_2: next position to put 2
        pos_put_0 = 0
        pos_put_2 = len_n - 1
        index = 0
        _____ index <= pos_put_2:
            __ nums[index] __ 0:
                nums[index], nums[pos_put_0] = nums[pos_put_0], nums[index]
                pos_put_0 += 1
                index += 1

            ____ nums[index] __ 2:
                nums[index], nums[pos_put_2] = nums[pos_put_2], nums[index]
                pos_put_2 -= 1

            ____
                index += 1

"""
[0]
[1,0]
[0,1,2]
[1,1,1,2,0,0,0,0,2,2,1,1,2]
"""
