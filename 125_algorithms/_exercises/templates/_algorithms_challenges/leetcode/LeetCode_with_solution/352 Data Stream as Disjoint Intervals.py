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
c_ Interval(o..
    ___ - , s=0, e=0
        start = s
        end = e


c_ SummaryRanges(o..
    ___ -
        """
        BST is the most efficient, while heap is simple to write
        Initialize your data structure here.
        """
        itvls    # list

    ___ addNum  val
        """
        O(lg n)
        :type val: int
        :rtype: void
        """
        itvls.a..(Interval(val, val

    ___ getIntervals
        """
        O(n lg n)
        :rtype: List[Interval]
        """
        itvls.s..(key=l.... x: x.start)

        ret = [itvls[0]]
        ___ itvl __ itvls[1:]:
            pre = ret[-1]
            __ itvl.start <= pre.end + 1:
                pre.end = m..(itvl.end, pre.end)
            ____
                ret.a..(itvl)

        itvls = ret
        r.. ret

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()