# -*- coding: utf-8 -*-
"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""


c_ Solution(o..
    ___ maxSubArray  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        # s[i] is sum of nums[0]..nums[i]
        # s[i] - s[j] is the sum of nums[j + 1] .. nums[i]
        s [0 ___ _ __ nums]
        ts 0  # temporary sum
        ___ i, c __ e..(nums
            ts += c
            s[i] ts
        min_sum 0
        res 0
        ___ i, c __ e..(s
            res m..(res, c - min_sum)
            min_sum m..(min_sum, c)
        __ res __ 0:
            r.. m..(nums)
        r.. res


a1 [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a2 [-1, -2, -3, -1]
a3 [1, 2]
s Solution()
print s.maxSubArray(a1)
print s.maxSubArray(a2)
print s.maxSubArray(a3)
