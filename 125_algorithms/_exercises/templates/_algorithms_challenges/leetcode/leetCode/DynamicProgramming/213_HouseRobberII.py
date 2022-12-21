#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Dynamic Programming
    ___ rob  nums
        __ n.. nums:
            r_ 0
        # We can break the circle according to whether rob house 0 or not.
        r_ m..(self.rob_line(nums[1:]),  # Not rob first house
                   self.rob_line(nums[2:-1]) + nums[0])  # Rob first house

    ___ rob_line  nums
        __ n.. nums:
            r_ 0
        pre_rob = nums[0]
        pre_not_rob = 0
        ___ num __ nums[1:]:
            cur_rob = pre_not_rob + num
            cur_not_rob = m..(pre_rob, pre_not_rob)
            pre_rob = cur_rob
            pre_not_rob = cur_not_rob
        r_ m..(pre_rob, pre_not_rob)

"""
[]
[1,2]
[12, 1,1,12,1]
"""
