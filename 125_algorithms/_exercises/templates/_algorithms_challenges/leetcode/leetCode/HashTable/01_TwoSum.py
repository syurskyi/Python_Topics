#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution_2 o..
    # Hashtable
    ___ twoSum  nums, target
        nums_dict _ # dict
        ___ index1, number1 __ enumerate(nums
            number2 = target - number1
            __ number2 __ nums_dict:
                r_ nums_dict[number2] + 1, index1 + 1
            nums_dict[number1] = index1

"""
[1,2]
3
[3,2,4]
6
"""
