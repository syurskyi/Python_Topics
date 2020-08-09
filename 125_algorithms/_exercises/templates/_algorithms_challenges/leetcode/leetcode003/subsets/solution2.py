class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S
        S.sort()
        r_ self.subsets_aux(S)

    ___ subsets_aux(self, S
        __ not S:
            r_ [[]]
        ____
            res = [[]]
            ___ i, e in enumerate(S
                rest_subsets = self.subsets_aux(S[i + 1:])
                ___ subset in rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            r_ res
