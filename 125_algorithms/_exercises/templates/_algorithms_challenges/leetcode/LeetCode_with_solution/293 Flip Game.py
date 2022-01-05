"""
Premium Question
Straightforward
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ generatePossibleNextMoves  s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret    # list
        ___ i __ xrange(l..(s)-1):
            __ s[i:i+2] __ "++":
                ret.a..(s[:i]+"--"+s[i+2:])

        r.. ret