# Using bit manipulation
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    ___ subsets(self, S
        S.sort()
        k = le.(S)
        n = 2 ** k
        res = []
        ___ i in range(n
            s = self.filter(S, k, i)
            res.append(s)
        r_ res

    ___ filter(self, S, k, i
        res = []
        ___ j in range(k
            mask = 1 << j
            __ i & mask > 0:
                res.append(S[j])
        r_ res

s = Solution()
print(s.subsets([1, 2, 3]))
