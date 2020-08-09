"""
Premium Question
Straightforward
"""
__author__ = 'Daniel'


class Solution(object
    ___ generatePossibleNextMoves(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        ___ i in xrange(le.(s)-1
            __ s[i:i+2] __ "++":
                ret.append(s[:i]+"--"+s[i+2:])

        r_ ret