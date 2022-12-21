#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
from collections import deque


c.. Solution o..
    # Implemented in array, slower than deque
    ___ maxSlidingWindow  nums, k
        max_num   # list
        queue   # list
        ___ i, v __ enumerate(nums
            # remove numbers out of range k
            __ queue a.. queue[0] __ i-k:
                queue = queue[1:]
            # remove smaller numbers in k range as they are useless
            _____ queue a.. v > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            __ i+1 >= k:
                max_num.append(nums[queue[0]])

        r_ max_num


c.. Solution_2 o..
    # Implemented in dqueue, much faster
    ___ maxSlidingWindow  nums, k
        max_num   # list
        queue = deque()
        ___ i, v __ enumerate(nums
            __ queue a.. queue[0] __ i-k:
                queue.popleft()
            _____ queue a.. v > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            __ i+1 >= k:
                max_num.append(nums[queue[0]])

        r_ max_num
"""
[]
0
[1,3,-1,-3,5,3,6,7]
3
[1,3,-1,-3,5,3,6,7]
2
"""
