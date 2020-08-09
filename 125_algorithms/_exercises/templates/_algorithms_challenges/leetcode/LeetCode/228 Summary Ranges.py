"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
__author__ = 'Daniel'


class Solution:
    ___ summaryRanges(self, nums
        """
        :type nums: list[int]
        :rtype: list[str]
        """
        ret = []
        n = le.(nums)
        __ n < 1:
            r_ ret

        bgn = nums[0]
        pre = nums[0]
        for i in xrange(1, n
            __ nums[i] != pre+1:
                __ pre != bgn:
                    ret.append("%d->%d"%(bgn, pre))
                ____
                    ret.append("%d"%bgn)
                bgn = nums[i]

            pre = nums[i]

        # clean up
        __ pre != bgn:
            ret.append("%d->%d"%(bgn, pre))
        ____
            ret.append("%d"%bgn)

        r_ ret


__ __name__ __ "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) __ ['0->2', '4->5', '7']