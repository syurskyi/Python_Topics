class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S):
        S.s..()
        r.. self.subsets_aux(S)

    ___ subsets_aux(self, S):
        __ n.. S:
            r.. [[]]
        ____:
            res = [[]]
            ___ i, e __ e..(S):
                rest_subsets = self.subsets_aux(S[i + 1:])
                ___ subset __ rest_subsets:
                    subset.insert(0, e)
                res += rest_subsets
            r.. res
