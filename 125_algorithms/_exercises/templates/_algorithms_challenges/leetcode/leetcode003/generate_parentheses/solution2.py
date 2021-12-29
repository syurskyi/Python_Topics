class Solution:
    # @param an integer
    # @return a list of string
    ___ generateParenthesis(self, n):
        cand    # list
        res    # list
        self.generate_paren_aux(n, n, cand, res)
        r.. res

    ___ generate_paren_aux(self, left, right, cand, res):
        __ left __ 0 a.. right __ 0:
            res.a..(''.join(cand))
        ____:
            __ left <= right a.. left > 0:
                cand.a..('(')
                self.generate_paren_aux(left - 1, right, cand, res)
                cand.pop()
            __ left < right a.. right > 0:
                cand.a..(')')
                self.generate_paren_aux(left, right - 1, cand, res)
                cand.pop()
