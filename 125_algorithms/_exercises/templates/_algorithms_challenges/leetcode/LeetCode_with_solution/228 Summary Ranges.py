"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
__author__ = 'Daniel'


c_ Solution:
    ___ summaryRanges(self, nums):
        """
        :type nums: list[int]
        :rtype: list[str]
        """
        ret    # list
        n = l..(nums)
        __ n < 1:
            r.. ret

        bgn = nums[0]
        pre = nums[0]
        ___ i __ xrange(1, n):
            __ nums[i] != pre+1:
                __ pre != bgn:
                    ret.a..("%d->%d"%(bgn, pre))
                ____:
                    ret.a..("%d"%bgn)
                bgn = nums[i]

            pre = nums[i]

        # clean up
        __ pre != bgn:
            ret.a..("%d->%d"%(bgn, pre))
        ____:
            ret.a..("%d"%bgn)

        r.. ret


__ _______ __ _______
    ... Solution().summaryRanges([0, 1, 2, 4, 5, 7]) __ ['0->2', '4->5', '7']