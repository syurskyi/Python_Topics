"""
Main Concept:
1. iterate from end, find the position to insert new one
2. append new one to `intvs`
3. iterate from end, and swap `intvs[i]` and `intvs[i - 1]`
   til meet the position found in (1)
4. iterate from start, do merge intv


Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


c_ Solution:
    ___ insert  intvs, intv
        """
        :type intvs: list[Interval]
        :type intv: Interval
        :rtype: list[Interval]
        """
        __ n.. intvs a.. n.. intv:
            r.. []
        __ n.. intvs:
            r.. [intv]
        __ n.. intv:
            r.. intvs

        ans    # list
        index = l..(intvs)

        ___ i __ r..(l..(intvs) - 1, -1, -1
            __ intvs[i].start <= intv.start:
                _____
            index -= 1

        intvs.a..(intv)
        ___ i __ r..(l..(intvs) - 1, index, -1
            intvs[i], intvs[i - 1] = intvs[i - 1], intvs[i]

        ___ i __ r..(l..(intvs:  # since there is one more child in intvs
            __ ans a.. intvs[i].start <= ans[-1].end:
                ans[-1].end = m..(ans[-1].end, intvs[i].end)
            ____
                ans.a..(intvs[i])

        r.. ans
