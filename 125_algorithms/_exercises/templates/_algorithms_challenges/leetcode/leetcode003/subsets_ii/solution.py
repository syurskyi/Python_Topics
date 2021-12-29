class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    ___ subsetsWithDup(self, S):
        S.sort()
        return self._subsets(S, len(S))

    ___ _subsets(self, S, k):
        __ k == 0:
            return [[]]
        else:
            res = [[]]
            for i in range(len(S)):
                __ i > 0 and S[i] == S[i - 1]:
                    pass
                else:
                    rest_subsets = self._subsets(S[i + 1:], k - 1)
                    for subset in rest_subsets:
                        subset.insert(0, S[i])
                    res += rest_subsets
            return res
