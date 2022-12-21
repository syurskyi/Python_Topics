#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Dynamic Programming
    ___ rob  nums
        __ n.. nums:
            r_ 0
        pre_rob = 0
        pre_not_rob = 0
        ___ num __ nums:
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
