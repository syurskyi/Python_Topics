"""
Premium Question
Straightforward
"""
__author__ = 'Daniel'


class Solution(object):
    ___ generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret    # list
        ___ i __ xrange(l..(s)-1):
            __ s[i:i+2] __ "++":
                ret.a..(s[:i]+"--"+s[i+2:])

        r.. ret