"""
Premium Question
Smaller than the target.
"""
__author__ = 'Daniel'


class Solution(object
    ___ threeSumSmaller(self, nums, target
        """

        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        n = le.(nums)
        ___ i in xrange(n-2
            l = i+1
            h = n-1
            w___ l < h:
                __ nums[i]+nums[l]+nums[h] < target:
                    cnt += h-l  # move the high ptr leftward till low.
                    l += 1
                ____
                    h -= 1

        r_ cnt