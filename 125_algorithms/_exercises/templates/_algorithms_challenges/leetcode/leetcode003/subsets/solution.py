class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S):
        S.sort()
        return self._subsets(S, len(S))

    ___ _subsets(self, S, k):
        __ k == 0:
            return [[]]
        else:
            res = [[]]
            for i in range(len(S)):
                rest_subsets = self._subsets(S[i + 1:], k - 1)
                for subset in rest_subsets:
                    subset.insert(0, S[i])
                res += rest_subsets
            return res
