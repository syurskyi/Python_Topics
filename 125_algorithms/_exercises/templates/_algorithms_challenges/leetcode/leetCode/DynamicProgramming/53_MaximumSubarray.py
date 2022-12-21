#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # O(n) space
    ___ maxSubArray  nums
        num_len = l..(nums)
        # dp[i]: Largest sum of contiguous subarray start from i
        dp = [-1] * num_len
        max_sum = dp[num_len - 1] = nums[num_len - 1]

        ___ i __ r..(num_len - 2, -1, -1
            dp[i] = m..(nums[i], dp[i+1]+nums[i])
            max_sum = m..(dp[i], max_sum)

        r_ max_sum


c.. Solution_2 o..
    # DP same with the previous, but O(1) space
    ___ maxSubArray  nums
        num_len = l..(nums)
        max_sum = pre_sum = nums[num_len - 1]

        ___ i __ r..(num_len - 2, -1, -1
            pre_sum = m..(nums[i], pre_sum+nums[i])
            max_sum = m..(pre_sum, max_sum)

        r_ max_sum

"""
[-1]
[1]
[-9,-2,-3,-5,-3]
[-2,1,-3,4,-1,2,1,-5,4]
"""
