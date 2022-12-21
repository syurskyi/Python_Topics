#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ moveZeroes  nums
        # Shift non-zero values as far forward as possible.
        index = 0
        ___ n __ nums:
            __ n != 0:
                nums[index] = n
                index += 1

        # Fill remaining space with zeros
        ___ i __ r..(index, l..(nums)):
            nums[i] = 0

        r_

"""
[]
[1]
[0]
[0,0,0]
[0,1,0,3,12]
[7,6,5,4,0,4,0,5,6,0,7,0,0]
"""
