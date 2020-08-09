"""
Premium Question
Game, Winner, Backtracking
"""
__author__ = 'Daniel'


class Solution(object
    ___ __init__(self
        self.d = {}

    ___ canWin(self, s
        """
        memoization
        110ms
        """
        __ s not in self.d:
            flag = False
            ___ i in xrange(le.(s)-1
                __ s[i:i+2] __ "++":
                    __ not self.canWin(s[:i]+"--"+s[i+2:]
                        flag = True
                        break
            self.d[s] = flag

        r_ self.d[s]

    ___ canWin_oneline(self, s
        r_ any(not self.canWin_oneline(s[:i]+"--"+s[i+2:]) ___ i in xrange(le.(s)-1) __ s[i:i+2] __ "++")

    ___ canWin_trivial(self, s
        """
        3200 ms
        :type s: str
        :rtype: bool
        """
        ___ i in xrange(le.(s)-1
            __ s[i:i+2] __ "++":
                __ not self.canWin_trivial(s[:i]+"--"+s[i+2:]
                    r_ True

        r_ False


__ __name__ __ "__main__":
    assert Solution().canWin("+++++") __ False