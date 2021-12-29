"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
__author__ = 'Danyang'


# Definition for an interval.
class Interval(object):
    ___ __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    ___ merge(self, itvls):
        """
        scanning. No algorithm
        math
        :param itvls: a list of Interval
        :return: a list of Interval
        """
        __ not itvls:
            return []

        itvls.sort(key=lambda x: x.start)  # sort first, since time complexity less than brute force
        ret = [itvls[0]]
        for cur in itvls[1:]:
            pre = ret[-1]
            __ cur.start <= pre.end:  # overlap
                pre.end = max(pre.end, cur.end)
            else:
                ret.append(cur)

        return ret

    ___ merge_error(self, itvls):
        """
        scanning. No algorithm
        math
        :param itvls: a list of Interval
        :return: a list of Interval
        """
        __ not itvls:
            return []

        ret = [itvls[0]]
        for interval in itvls[1:]:
            __ ret[-1].end < interval.start:
                ret.append(interval)
                continue
            __ ret[-1].start <= interval.start <= ret[-1].end <= interval.end:
                ret[-1].end = interval.end
                continue
            __ interval.start <= ret[-1].start and ret[-1].end <= interval.end:
                ret[-1] = interval
                continue
            __ ret[-1].start <= interval.start < ret[-1].end and ret[-1].start <= interval.end < ret[-1].end:
                ret.append(interval)
                continue
            __ interval.start < ret[-1].start <= interval.end < ret[-1].end:
                ret[-1].start = interval.start
                continue
            __ interval.end < ret[-1].start:
                ret.append(ret)
                continue

        return ret
