class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum(self, candidates, target
        res = []
        cand = []
        candidates.sort()
        self.combination_sum(candidates, cand, target, res)
        r_ res

    ___ combination_sum(self, candidates, cand, target, res
        __ target < 0:
            r_
        ____ target __ 0:
            res.append(cand[:])
        ____
            ___ i, c in enumerate(candidates
                cand.append(c)
                self.combination_sum(candidates[i:], cand, target - c, res)
                cand.p..
