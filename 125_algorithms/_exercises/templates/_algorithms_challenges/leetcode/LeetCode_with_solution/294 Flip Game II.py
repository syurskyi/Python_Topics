"""
Premium Question
Game, Winner, Backtracking
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ - ):
        d    # dict

    ___ canWin(self, s):
        """
        memoization
        110ms
        """
        __ s n.. __ d:
            flag = F..
            ___ i __ xrange(l..(s)-1):
                __ s[i:i+2] __ "++":
                    __ n.. canWin(s[:i]+"--"+s[i+2:]):
                        flag = T..
                        break
            d[s] = flag

        r.. d[s]

    ___ canWin_oneline(self, s):
        r.. any(n.. canWin_oneline(s[:i]+"--"+s[i+2:]) ___ i __ xrange(l..(s)-1) __ s[i:i+2] __ "++")

    ___ canWin_trivial(self, s):
        """
        3200 ms
        :type s: str
        :rtype: bool
        """
        ___ i __ xrange(l..(s)-1):
            __ s[i:i+2] __ "++":
                __ n.. canWin_trivial(s[:i]+"--"+s[i+2:]):
                    r.. T..

        r.. F..


__ __name__ __ "__main__":
    ... Solution().canWin("+++++") __ F..