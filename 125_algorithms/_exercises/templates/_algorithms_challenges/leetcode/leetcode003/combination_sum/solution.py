class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum(self, candidates, target):
        res = []
        cand = []
        candidates.sort()
        self.combination_sum(candidates, cand, target, res)
        return res

    ___ combination_sum(self, candidates, cand, target, res):
        __ target < 0:
            return
        elif target == 0:
            res.append(cand[:])
        else:
            for i, c in enumerate(candidates):
                cand.append(c)
                self.combination_sum(candidates[i:], cand, target - c, res)
                cand.pop()
