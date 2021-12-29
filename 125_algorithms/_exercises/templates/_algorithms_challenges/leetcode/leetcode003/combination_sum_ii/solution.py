class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        cand = []
        self.combination_sum(candidates, target, cand, res)
        return res

    ___ combination_sum(self, candidates, target, cand, res):
        __ target == 0:
            res.append(cand[:])
        elif target < 0:
            return
        else:
            for i, c in enumerate(candidates):
                __ i == 0:
                    prev = c
                elif prev == c:
                    continue
                else:
                    prev = c
                cand.append(c)
                self.combination_sum(candidates[i + 1:], target - c, cand, res)
                cand.pop()
