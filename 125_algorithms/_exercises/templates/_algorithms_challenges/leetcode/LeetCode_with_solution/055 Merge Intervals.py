"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
__author__ 'Danyang'


# Definition for an interval.
c_ Interval(o..
    ___ - , s=0, e=0
        start s
        end e


c_ Solution(o..
    ___ merge  itvls
        """
        scanning. No algorithm
        math
        :param itvls: a list of Interval
        :return: a list of Interval
        """
        __ n.. itvls:
            r.. []

        itvls.s..(k.._l.... x: x.start)  # sort first, since time complexity less than brute force
        ret [itvls[0]]
        ___ cur __ itvls[1:]:
            pre ret[-1]
            __ cur.start <_ pre.end:  # overlap
                pre.end m..(pre.end, cur.end)
            ____
                ret.a..(cur)

        r.. ret

    ___ merge_error  itvls
        """
        scanning. No algorithm
        math
        :param itvls: a list of Interval
        :return: a list of Interval
        """
        __ n.. itvls:
            r.. []

        ret [itvls[0]]
        ___ interval __ itvls[1:]:
            __ ret[-1].end < interval.start:
                ret.a..(interval)
                _____
            __ ret[-1].start <_ interval.start <_ ret[-1].end <_ interval.end:
                ret[-1].end interval.end
                _____
            __ interval.start <_ ret[-1].start a.. ret[-1].end <_ interval.end:
                ret[-1] interval
                _____
            __ ret[-1].start <_ interval.start < ret[-1].end a.. ret[-1].start <_ interval.end < ret[-1].end:
                ret.a..(interval)
                _____
            __ interval.start < ret[-1].start <_ interval.end < ret[-1].end:
                ret[-1].start interval.start
                _____
            __ interval.end < ret[-1].start:
                ret.a..(ret)
                _____

        r.. ret
