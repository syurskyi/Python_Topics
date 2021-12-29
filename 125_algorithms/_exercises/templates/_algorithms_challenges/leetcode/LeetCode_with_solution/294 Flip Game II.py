"""
Premium Question
Game, Winner, Backtracking
"""
__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.d = {}

    ___ canWin(self, s):
        """
        memoization
        110ms
        """
        __ s n.. __ self.d:
            flag = False
            ___ i __ xrange(l..(s)-1):
                __ s[i:i+2] __ "++":
                    __ n.. self.canWin(s[:i]+"--"+s[i+2:]):
                        flag = True
                        break
            self.d[s] = flag

        r.. self.d[s]

    ___ canWin_oneline(self, s):
        r.. any(n.. self.canWin_oneline(s[:i]+"--"+s[i+2:]) ___ i __ xrange(l..(s)-1) __ s[i:i+2] __ "++")

    ___ canWin_trivial(self, s):
        """
        3200 ms
        :type s: str
        :rtype: bool
        """
        ___ i __ xrange(l..(s)-1):
            __ s[i:i+2] __ "++":
                __ n.. self.canWin_trivial(s[:i]+"--"+s[i+2:]):
                    r.. True

        r.. False


__ __name__ __ "__main__":
    ... Solution().canWin("+++++") __ False