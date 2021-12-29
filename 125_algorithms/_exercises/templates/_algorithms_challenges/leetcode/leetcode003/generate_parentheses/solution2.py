class Solution:
    # @param an integer
    # @return a list of string
    ___ generateParenthesis(self, n):
        cand = []
        res = []
        self.generate_paren_aux(n, n, cand, res)
        return res

    ___ generate_paren_aux(self, left, right, cand, res):
        __ left == 0 and right == 0:
            res.append(''.join(cand))
        else:
            __ left <= right and left > 0:
                cand.append('(')
                self.generate_paren_aux(left - 1, right, cand, res)
                cand.pop()
            __ left < right and right > 0:
                cand.append(')')
                self.generate_paren_aux(left, right - 1, cand, res)
                cand.pop()
