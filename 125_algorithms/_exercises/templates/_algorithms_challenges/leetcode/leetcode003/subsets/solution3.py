c_ Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets  S):
        S.s..()
        cand    # list
        res    # list
        subsets_aux(S, cand, res)
        r.. res

    ___ subsets_aux  S, cand, res):
        res.a..(cand | )
        ___ i, e __ e..(S):
            cand.a..(S[i])
            subsets_aux(S[i + 1:], cand, res)
            cand.pop()

s = Solution()
print(s.subsets([1, 2, 3]))
