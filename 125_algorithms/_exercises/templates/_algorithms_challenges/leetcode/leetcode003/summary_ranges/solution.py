"""
Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
    ___ summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        start = -1
        end = -1
        for i, e in enumerate(nums):
            __ i == 0:
                start = 0
                end = 0
            else:
                __ e != nums[i - 1] + 1:
                    r = self.make_range(start, end, nums)
                    res.append(r)
                    start = i
                end = i
            __ i == n - 1:
                end = i
                r = self.make_range(start, end, nums)
                res.append(r)
        return res

    ___ make_range(self, start, end, nums):
        __ end > start:
            return "%d->%d" % (nums[start], nums[end])
        elif end == start:
            return "%d" % nums[end]


a1 = [0, 1, 2, 4, 5, 7]
a2 = [0, 5, 9]
s = Solution()
print(s.summaryRanges(a1))
print(s.summaryRanges(a2))
