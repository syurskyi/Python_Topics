"""
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers. You
may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    ___ threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = l..(nums)
        res = nums[0] + nums[1] + nums[2]
        ___ i __ r..(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                __ abs(s - target) < abs(res - target):
                    res = s
                __ s __ target:
                    r.. s
                ____ s < target:
                    l += 1
                ____:
                    r -= 1
        r.. res
