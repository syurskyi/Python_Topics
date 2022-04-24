c_ Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets  S
        S.s..()
        r.. subsets_aux(S)

    ___ subsets_aux  S
        __ n.. S:
            r.. [[]]
        ____
            res [[]]
            ___ i, e __ e..(S
                rest_subsets subsets_aux(S[i + 1:])
                ___ subset __ rest_subsets:
                    subset.i.. 0, e)
                res += rest_subsets
            r.. res
