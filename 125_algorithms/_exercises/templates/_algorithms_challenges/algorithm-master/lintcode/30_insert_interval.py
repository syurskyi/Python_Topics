"""
Main Concept:
1. iterate from end, find the position to insert new one
2. append new one to `intvs`
3. iterate from end, and swap `intvs[i]` and `intvs[i - 1]`
   til meet the position found in (1)
4. iterate from start, do merge intv


Definition of Interval.
class Interval(object
    ___ __init__(self, start, end
        self.start = start
        self.end = end
"""


class Solution:
    ___ insert(self, intvs, intv
        """
        :type intvs: list[Interval]
        :type intv: Interval
        :rtype: list[Interval]
        """
        __ not intvs and not intv:
            r_ []
        __ not intvs:
            r_ [intv]
        __ not intv:
            r_ intvs

        ans = []
        index = le.(intvs)

        ___ i in range(le.(intvs) - 1, -1, -1
            __ intvs[i].start <= intv.start:
                break
            index -= 1

        intvs.append(intv)
        ___ i in range(le.(intvs) - 1, index, -1
            intvs[i], intvs[i - 1] = intvs[i - 1], intvs[i]

        ___ i in range(le.(intvs)):  # since there is one more child in intvs
            __ ans and intvs[i].start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, intvs[i].end)
            ____
                ans.append(intvs[i])

        r_ ans
