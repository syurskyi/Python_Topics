"""
Premium Question
Smaller than the target.
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ threeSumSmaller(self, nums, target):
        """

        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        nums.s..()
        cnt = 0
        n = l..(nums)
        ___ i __ xrange(n-2):
            l = i+1
            h = n-1
            w.... l < h:
                __ nums[i]+nums[l]+nums[h] < target:
                    cnt += h-l  # move the high ptr leftward till low.
                    l += 1
                ____:
                    h -= 1

        r.. cnt