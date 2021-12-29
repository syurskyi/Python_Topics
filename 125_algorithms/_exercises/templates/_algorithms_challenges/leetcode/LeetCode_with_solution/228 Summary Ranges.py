"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
__author__ = 'Daniel'


class Solution:
    ___ summaryRanges(self, nums):
        """
        :type nums: list[int]
        :rtype: list[str]
        """
        ret = []
        n = len(nums)
        __ n < 1:
            return ret

        bgn = nums[0]
        pre = nums[0]
        for i in xrange(1, n):
            __ nums[i] != pre+1:
                __ pre != bgn:
                    ret.append("%d->%d"%(bgn, pre))
                else:
                    ret.append("%d"%bgn)
                bgn = nums[i]

            pre = nums[i]

        # clean up
        __ pre != bgn:
            ret.append("%d->%d"%(bgn, pre))
        else:
            ret.append("%d"%bgn)

        return ret


__ __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ['0->2', '4->5', '7']