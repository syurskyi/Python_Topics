#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ moveZeroes  nums
        # Get sum of zeros
        count = 0
        ___ num __ nums:
            __ n.. num:
                count += 1

        # Move the no-zero number to the right position.
        pos, i = 0, 0
        _____ pos < l..(nums
            __ nums[pos]:
                nums[i] = nums[pos]
                i += 1
            pos += 1

        # Append the zeros
        __ count:
            nums[-count:] = [0] * count
        r_

"""
[]
[1]
[0]
[0,0,0]
[0,1,0,3,12]
[7,6,5,4,0,4,0,5,6,0,7,0,0]
"""
