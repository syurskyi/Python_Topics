"""
Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

c_ Solution(o..
    ___ summaryRanges  nums
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res    # list
        n l..(nums)
        start -1
        end -1
        ___ i, e __ e..(nums
            __ i __ 0:
                start 0
                end 0
            ____
                __ e !_ nums[i - 1] + 1:
                    r make_range(start, end, nums)
                    res.a..(r)
                    start i
                end i
            __ i __ n - 1:
                end i
                r make_range(start, end, nums)
                res.a..(r)
        r.. res

    ___ make_range  start, end, nums
        __ end > start:
            r.. "_d->_d" % (nums[start], nums[end])
        ____ end __ start:
            r.. "_d" % nums[end]


a1 [0, 1, 2, 4, 5, 7]
a2 [0, 5, 9]
s Solution()
print(s.summaryRanges(a1
print(s.summaryRanges(a2
