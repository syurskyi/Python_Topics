c_ Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    ___ combinationSum2  candidates, target):
        candidates.s..()
        res    # list
        cand    # list
        combination_sum(candidates, target, cand, res)
        r.. res

    ___ combination_sum  candidates, target, cand, res):
        __ target __ 0:
            res.a..(cand | )
        ____ target < 0:
            r..
        ____:
            ___ i, c __ e..(candidates):
                __ i __ 0:
                    prev = c
                ____ prev __ c:
                    _____
                ____:
                    prev = c
                cand.a..(c)
                combination_sum(candidates[i + 1:], target - c, cand, res)
                cand.pop()
