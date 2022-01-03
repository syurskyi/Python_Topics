c_ Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum2(self, candidates, target):
        candidates.s..()
        res    # list
        cand    # list
        combination_sum_aux(candidates, target, cand, res)
        r.. res

    ___ combination_sum_aux(self, candidates, target, cand, res):
        __ target __ 0:
            res.a..(cand[:])
        ____:
            prev = N..
            ___ i, c __ e..(candidates):
                __ prev __ N.. o. prev != c:
                    __ target - c >= 0:
                        cand.a..(c)
                        combination_sum_aux(candidates[i + 1:],
                                                 target - c, cand, res)
                        cand.pop()
                prev = c
