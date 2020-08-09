"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not
get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the
neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous
street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""
__author__ = 'Daniel'


class Solution:
    ___ rob(self, nums
        """
        Two cases: cannot touch 1st element vs. cannot touch 2nd element.
        There are two cases here 1) 1st element is included and last is not included 2) 1st is not included and last is
        included.
        :type nums: list
        :rtype: int
        """
        n = le.(nums)
        __ n < 2:
            r_ su.(nums)

        # include first but exclude last
        F = [0 ___ _ in xrange(n-1+2)]
        ___ i in xrange(2, n+1
            F[i] = max(F[i-1], F[i-2]+nums[i-2])
        ret = F[-1]

        # exclude first but include last
        F = [0 ___ _ in xrange(n-1+2)]
        ___ i in xrange(2, n+1
            F[i] = max(F[i-1], F[i-2]+nums[i-1])

        ret = max(ret, F[-1])
        r_ ret
