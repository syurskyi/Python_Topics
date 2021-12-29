class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum2(self, candidates, target):
        candidates.sort()
        res    # list
        cand    # list
        self.combination_sum(candidates, target, cand, res)
        r.. res

    ___ combination_sum(self, candidates, target, cand, res):
        __ target __ 0:
            res.a..(cand[:])
        ____ target < 0:
            r..
        ____:
            ___ i, c __ enumerate(candidates):
                __ i __ 0:
                    prev = c
                ____ prev __ c:
                    continue
                ____:
                    prev = c
                cand.a..(c)
                self.combination_sum(candidates[i + 1:], target - c, cand, res)
                cand.pop()
