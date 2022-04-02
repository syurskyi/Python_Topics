# -*- coding: utf-8 -*-
# Time Limit Exceeded
"""
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which
gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b
≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""


c_ Solution(o..
    ___ fourSum  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = l..(nums)
        nums.s..()
        res    # list
        ___ a __ r..(n - 3
            __ a > 0 a.. nums[a - 1] __ nums[a]:
                _____
            ___ b __ r..(a + 1, n - 2
                __ b > a + 1 a.. nums[b - 1] __ nums[b]:
                    _____
                c = b + 1
                d = n - 1
                w.... c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    __ s __ target:
                        res.a..([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        w.... c < d a.. nums[c] __ nums[c - 1]:
                            c += 1
                        w.... c < d a.. nums[d] __ nums[d + 1]:
                            d -= 1
                    ____ s < target:
                        c += 1
                    ____:
                        d -= 1
        r.. res
