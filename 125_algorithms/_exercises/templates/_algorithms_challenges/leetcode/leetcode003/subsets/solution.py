class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S
        S.sort()
        r_ self._subsets(S, le.(S))

    ___ _subsets(self, S, k
        __ k __ 0:
            r_ [[]]
        ____
            res = [[]]
            for i in range(le.(S)):
                rest_subsets = self._subsets(S[i + 1:], k - 1)
                for subset in rest_subsets:
                    subset.insert(0, S[i])
                res += rest_subsets
            r_ res
