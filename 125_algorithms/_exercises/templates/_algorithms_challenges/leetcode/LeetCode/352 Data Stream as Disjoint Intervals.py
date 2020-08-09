"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of
disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""
__author__ = 'Daniel'


# Definition for an interval.
class Interval(object
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e


class SummaryRanges(object
    ___ __init__(self
        """
        BST is the most efficient, w___ heap is simple to write
        Initialize your data structure here.
        """
        self.itvls = []

    ___ addNum(self, val
        """
        O(lg n)
        :type val: int
        :rtype: void
        """
        self.itvls.append(Interval(val, val))

    ___ getIntervals(self
        """
        O(n lg n)
        :rtype: List[Interval]
        """
        self.itvls.sort(key=lambda x: x.start)

        ret = [self.itvls[0]]
        ___ itvl in self.itvls[1:]:
            pre = ret[-1]
            __ itvl.start <= pre.end + 1:
                pre.end = max(itvl.end, pre.end)
            ____
                ret.append(itvl)

        self.itvls = ret
        r_ ret

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()