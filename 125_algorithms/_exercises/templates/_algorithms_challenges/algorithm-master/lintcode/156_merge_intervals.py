"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


c_ Solution:
    ___ merge(self, intvs):
        """
        :type intvs: List[Interval]
        :rtype: List[Interval]
        """
        ans    # list
        __ n.. intvs:
            r.. ans

        intvs.s..(key=l.... intv: (intv.start, intv.end))

        ___ intv __ intvs:
            __ n.. ans o. intv.start > ans[-1].end:
                ans.a..(intv)
            ____ intv.end > ans[-1].end:
                ans[-1].end = intv.end

        r.. ans
