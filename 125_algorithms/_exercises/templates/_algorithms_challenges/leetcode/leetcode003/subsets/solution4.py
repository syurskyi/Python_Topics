# Using bit manipulation
c_ Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S):
        S.s..()
        k = l..(S)
        n = 2 ** k
        res    # list
        ___ i __ r..(n):
            s = filter(S, k, i)
            res.a..(s)
        r.. res

    ___ filter(self, S, k, i):
        res    # list
        ___ j __ r..(k):
            mask = 1 << j
            __ i & mask > 0:
                res.a..(S[j])
        r.. res

s = Solution()
print(s.subsets([1, 2, 3]))
