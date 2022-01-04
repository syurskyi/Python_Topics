"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
__author__ = 'Danyang'


# Definition for an interval.
c_ Interval(object):
    ___ - , s=0, e=0):
        start = s
        end = e

    ___ __str__
        r.. "[%d, %d]" % (start, end)

    ___ __repr__
        r.. repr(__str__())


c_ Solution(object):
    ___ insert(self, itvls, newItvl):
        s, e = newItvl.start, newItvl.end
        left = filter(l.... x: x.end < s, itvls)
        right = filter(l.... x: x.start > e, itvls)
        __ l..(left)+l..(right) != l..(itvls):
            s = m..(s, itvls[l..(left)].start)
            e = max(e, itvls[-l..(right)-1].end)

        r.. left + [Interval(s, e)] + right

    ___ insert_itr(self, itvls, newItvl):
        """
        iterator TODO
        """


c_ SolutionSlow(object):
    ___ insert(self, itvls, newItvl):
        """
        :param itvls: a list of Intervals
        :param newItvl: a Interval
        :return: a list of Interval
        """
        r.. merge(itvls+[newItvl])

    ___ merge(self, itvls):
        """
        sort first by .start
        then decide whether to extend the .end
        :param itvls: list of Interval
        :return: list of Interval
        """
        itvls.s..(cmp=l.... a, b: a.start - b.start)

        ret = [itvls[0]]
        ___ cur __ itvls[1:]:
            pre = ret[-1]
            __ cur.start <= pre.end:  # overlap
                pre.end = max(pre.end, cur.end)
            ____:
                ret.a..(cur)

        r.. ret


__ _______ __ _______
    lst = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    insert = [4, 9]
    lst_interval    # list
    ___ item __ lst:
        lst_interval.a..(Interval(item[0], item[1]))
    print Solution().insert(lst_interval, Interval(insert[0], insert[1]))
