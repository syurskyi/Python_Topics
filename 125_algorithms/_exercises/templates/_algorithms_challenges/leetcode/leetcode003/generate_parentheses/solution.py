class Solution:
    # @param an integer
    # @return a list of string
    ___ generateParenthesis(self, n):
        res    # list
        cand = ''
        self.gp(n, n, cand, res)
        r.. res

    ___ gp(self, left, right, cand, res):
        __ left > right o. left < 0:
            r..
        ____ left __ 0 a.. right __ 0:
            res.a..(cand)
        ____:
            self.gp(left - 1, right, cand + '(', res)
            self.gp(left, right - 1, cand + ')', res)
