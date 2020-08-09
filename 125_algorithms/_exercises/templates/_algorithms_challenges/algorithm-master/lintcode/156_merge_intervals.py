"""
Definition of Interval.
class Interval(object
    ___ __init__(self, start, end
        self.start = start
        self.end = end
"""


class Solution:
    ___ merge(self, intvs
        """
        :type intvs: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        __ not intvs:
            r_ ans

        intvs.sort(key=lambda intv: (intv.start, intv.end))

        for intv in intvs:
            __ not ans or intv.start > ans[-1].end:
                ans.append(intv)
            ____ intv.end > ans[-1].end:
                ans[-1].end = intv.end

        r_ ans
