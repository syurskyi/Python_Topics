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
class Interval(object
    ___ __init__(self, s=0, e=0
        self.start = s
        self.end = e

    ___ __str__(self
        r_ "[%d, %d]" % (self.start, self.end)

    ___ __repr__(self
        r_ repr(self.__str__())


class Solution(object
    ___ insert(self, itvls, newItvl
        s, e = newItvl.start, newItvl.end
        left = filter(lambda x: x.end < s, itvls)
        right = filter(lambda x: x.start > e, itvls)
        __ le.(left)+le.(right) != le.(itvls
            s = min(s, itvls[le.(left)].start)
            e = ma.(e, itvls[-le.(right)-1].end)

        r_ left + [Interval(s, e)] + right

    ___ insert_itr(self, itvls, newItvl
        """
        iterator TODO
        """


class SolutionSlow(object
    ___ insert(self, itvls, newItvl
        """
        :param itvls: a list of Intervals
        :param newItvl: a Interval
        :return: a list of Interval
        """
        r_ self.merge(itvls+[newItvl])

    ___ merge(self, itvls
        """
        sort first by .start
        then decide whether to extend the .end
        :param itvls: list of Interval
        :return: list of Interval
        """
        itvls.sort(cmp=lambda a, b: a.start - b.start)

        ret = [itvls[0]]
        ___ cur __ itvls[1:]:
            pre = ret[-1]
            __ cur.start <= pre.end:  # overlap
                pre.end = ma.(pre.end, cur.end)
            ____
                ret.append(cur)

        r_ ret


__  -n __ "__main__":
    lst = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    insert = [4, 9]
    lst_interval =   # list
    ___ item __ lst:
        lst_interval.append(Interval(item[0], item[1]))
    print Solution().insert(lst_interval, Interval(insert[0], insert[1]))
