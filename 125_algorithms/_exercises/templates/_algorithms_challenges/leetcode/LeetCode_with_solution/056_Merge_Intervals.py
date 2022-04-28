# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

c_ Solution o..
    ___ merge  intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        __ intervals is N..:
            r_
        ls = l.. intervals)
        __ ls <= 1:
            r_ intervals
        # sort by start
        intervals.sort(key=lambda x: x.start)
        pos = 0
        w.. pos < l.. intervals) - 1:
            # check overlap
            __ intervals[pos].end >= intervals[pos + 1].start:
                next = intervals.pop(pos + 1)
                # check next is overlap or totally covered by pos
                __ next.end > intervals[pos].end:
                    intervals[pos].end = next.end
            # print [(t.start, t.end) for t in intervals], pos
            ____
                pos += 1
        r_ intervals

__ ____ __ ____
    # begin
    s  ?
    print s.merge([[1,3],[2,6],[8,10],[15,18]])