class Solution:
    # @param an integer
    # @return a list of string
    ___ generateParenthesis(self, n
        cand =   # list
        res =   # list
        self.generate_paren_aux(n, n, cand, res)
        r_ res

    ___ generate_paren_aux(self, left, right, cand, res
        __ left __ 0 and right __ 0:
            res.append(''.join(cand))
        ____
            __ left <= right and left > 0:
                cand.append('(')
                self.generate_paren_aux(left - 1, right, cand, res)
                cand.p..
            __ left < right and right > 0:
                cand.append(')')
                self.generate_paren_aux(left, right - 1, cand, res)
                cand.p..
