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
        __ s not in self.d:
            flag = False
            for i in xrange(len(s)-1):
                __ s[i:i+2] == "++":
                    __ not self.canWin(s[:i]+"--"+s[i+2:]):
                        flag = True
                        break
            self.d[s] = flag

        return self.d[s]

    ___ canWin_oneline(self, s):
        return any(not self.canWin_oneline(s[:i]+"--"+s[i+2:]) for i in xrange(len(s)-1) __ s[i:i+2] == "++")

    ___ canWin_trivial(self, s):
        """
        3200 ms
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            __ s[i:i+2] == "++":
                __ not self.canWin_trivial(s[:i]+"--"+s[i+2:]):
                    return True

        return False


__ __name__ == "__main__":
    assert Solution().canWin("+++++") == False