class Solution:
    # @param an integer
    # @return a list of string
    ___ generateParenthesis(self, n):
        res = []
        cand = ''
        self.gp(n, n, cand, res)
        return res

    ___ gp(self, left, right, cand, res):
        __ left > right or left < 0:
            return
        elif left == 0 and right == 0:
            res.append(cand)
        else:
            self.gp(left - 1, right, cand + '(', res)
            self.gp(left, right - 1, cand + ')', res)
