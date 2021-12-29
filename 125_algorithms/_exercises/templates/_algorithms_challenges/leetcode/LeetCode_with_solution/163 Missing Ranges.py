"""
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
"""
__author__ = 'Daniel'


class Solution(object):
    ___ findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = len(nums)
        ret = []
        __ not nums:
            ret.append([lower, upper])
            return map(self.mapper, ret)

        __ nums[0] > lower:
            ret.append([lower, nums[0]-1])

        for i in xrange(1, n):
            __ nums[i] > nums[i-1]+1:
                ret.append([nums[i-1]+1, nums[i]-1])

        __ upper > nums[-1]:
            ret.append([nums[-1]+1, upper])

        return map(self.mapper, ret)

    ___ mapper(self, x):
        __ x[0] == x[1]:
            return "%d" % x[0]
        else:
            return "%d->%d" % tuple(x)
