class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        cand = []
        self.combination_sum_aux(candidates, target, cand, res)
        return res

    ___ combination_sum_aux(self, candidates, target, cand, res):
        __ target == 0:
            res.append(cand[:])
        else:
            prev = None
            for i, c in enumerate(candidates):
                __ prev is None or prev != c:
                    __ target - c >= 0:
                        cand.append(c)
                        self.combination_sum_aux(candidates[i + 1:],
                                                 target - c, cand, res)
                        cand.pop()
                prev = c
