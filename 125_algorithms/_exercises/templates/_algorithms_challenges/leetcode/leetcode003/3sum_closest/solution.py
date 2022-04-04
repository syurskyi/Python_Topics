"""
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers. You
may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


c_ Solution(o..
    ___ threeSumClosest  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.s..()
        n = l..(nums)
        res = nums[0] + nums[1] + nums[2]
        ___ i __ r..(n - 2
            l = i + 1
            r = n - 1
            w.... l < r:
                s = nums[i] + nums[l] + nums[r]
                __ a..(s - target) < a..(res - target
                    res = s
                __ s __ target:
                    r.. s
                ____ s < target:
                    l += 1
                ____
                    r -= 1
        r.. res
