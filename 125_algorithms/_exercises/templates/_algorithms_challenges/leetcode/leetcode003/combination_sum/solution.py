class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum(self, candidates, target):
        res    # list
        cand    # list
        candidates.s..()
        self.combination_sum(candidates, cand, target, res)
        r.. res

    ___ combination_sum(self, candidates, cand, target, res):
        __ target < 0:
            r..
        ____ target __ 0:
            res.a..(cand[:])
        ____:
            ___ i, c __ e..(candidates):
                cand.a..(c)
                self.combination_sum(candidates[i:], cand, target - c, res)
                cand.pop()
