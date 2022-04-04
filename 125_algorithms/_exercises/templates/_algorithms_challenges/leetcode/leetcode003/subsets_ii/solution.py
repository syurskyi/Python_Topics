c_ Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    ___ subsetsWithDup  S
        S.s..()
        r.. _subsets(S, l..(S

    ___ _subsets  S, k
        __ k __ 0:
            r.. [[]]
        ____:
            res = [[]]
            ___ i __ r..(l..(S:
                __ i > 0 a.. S[i] __ S[i - 1]:
                    p..
                ____:
                    rest_subsets = _subsets(S[i + 1:], k - 1)
                    ___ subset __ rest_subsets:
                        subset.insert(0, S[i])
                    res += rest_subsets
            r.. res
