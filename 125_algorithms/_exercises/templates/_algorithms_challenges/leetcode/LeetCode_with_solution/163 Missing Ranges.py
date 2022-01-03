"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = l..(nums)
        ret    # list
        __ n.. nums:
            ret.a..([lower, upper])
            r.. map(mapper, ret)

        __ nums[0] > lower:
            ret.a..([lower, nums[0]-1])

        ___ i __ xrange(1, n):
            __ nums[i] > nums[i-1]+1:
                ret.a..([nums[i-1]+1, nums[i]-1])

        __ upper > nums[-1]:
            ret.a..([nums[-1]+1, upper])

        r.. map(mapper, ret)

    ___ mapper(self, x):
        __ x[0] __ x[1]:
            r.. "%d" % x[0]
        ____:
            r.. "%d->%d" % tuple(x)
