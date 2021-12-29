# -*- coding: utf-8 -*-
"""
Given an array S of n integers, are there elements a, b, c in S such that a +
b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""


class Solution(object):
    ___ threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.s..()
        res    # list
        ___ i __ r..(l..(nums) - 2):
            __ i __ 0 o. i > 0 a.. nums[i - 1] != nums[i]:
                left = i + 1
                right = l..(nums) - 1
                w.... left < right:
                    s = nums[i] + nums[left] + nums[right]
                    __ s __ 0:
                        res.a..([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        w.... left < right a.. nums[left] __ nums[left - 1]:
                            left += 1
                        w.... right > left a.. nums[right] __ nums[right + 1]:
                            right -= 1
                    ____ s < 0:
                        left += 1
                    ____:
                        right -= 1
        r.. res
