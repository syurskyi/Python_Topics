class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S
        S.sort()
        cand = []
        res = []
        self.subsets_aux(S, cand, res)
        r_ res

    ___ subsets_aux(self, S, cand, res
        res.append(cand[:])
        ___ i, e in enumerate(S
            cand.append(S[i])
            self.subsets_aux(S[i + 1:], cand, res)
            cand.p..

s = Solution()
print(s.subsets([1, 2, 3]))
