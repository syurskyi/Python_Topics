class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum2(self, candidates, target
        candidates.sort()
        res = []
        cand = []
        self.combination_sum(candidates, target, cand, res)
        r_ res

    ___ combination_sum(self, candidates, target, cand, res
        __ target __ 0:
            res.append(cand[:])
        ____ target < 0:
            r_
        ____
            ___ i, c in enumerate(candidates
                __ i __ 0:
                    prev = c
                ____ prev __ c:
                    continue
                ____
                    prev = c
                cand.append(c)
                self.combination_sum(candidates[i + 1:], target - c, cand, res)
                cand.pop()
