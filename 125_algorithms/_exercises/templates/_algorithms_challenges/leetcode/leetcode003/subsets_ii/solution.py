class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    ___ subsetsWithDup(self, S
        S.sort()
        r_ self._subsets(S, le.(S))

    ___ _subsets(self, S, k
        __ k __ 0:
            r_ [[]]
        ____
            res = [[]]
            for i in range(le.(S)):
                __ i > 0 and S[i] __ S[i - 1]:
                    pass
                ____
                    rest_subsets = self._subsets(S[i + 1:], k - 1)
                    for subset in rest_subsets:
                        subset.insert(0, S[i])
                    res += rest_subsets
            r_ res
