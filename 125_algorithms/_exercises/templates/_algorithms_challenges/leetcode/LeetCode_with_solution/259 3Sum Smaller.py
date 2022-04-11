"""
Premium Question
Smaller than the target.
"""
__author__ 'Daniel'


c_ Solution(o..
    ___ threeSumSmaller  nums, target
        """

        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        nums.s..()
        cnt 0
        n l..(nums)
        ___ i __ x..(n-2
            l i+1
            h n-1
            w.... l < h:
                __ nums[i]+nums[l]+nums[h] < target:
                    cnt += h-l  # move the high ptr leftward till low.
                    l += 1
                ____
                    h -_ 1

        r.. cnt