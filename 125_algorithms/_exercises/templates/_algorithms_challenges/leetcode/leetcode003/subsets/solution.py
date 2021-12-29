class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S):
        S.s..()
        r.. self._subsets(S, l..(S))

    ___ _subsets(self, S, k):
        __ k __ 0:
            r.. [[]]
        ____:
            res = [[]]
            ___ i __ r..(l..(S)):
                rest_subsets = self._subsets(S[i + 1:], k - 1)
                ___ subset __ rest_subsets:
                    subset.insert(0, S[i])
                res += rest_subsets
            r.. res
