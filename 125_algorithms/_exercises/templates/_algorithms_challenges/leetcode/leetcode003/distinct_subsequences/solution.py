class Solution:
    # @return an integer
    ___ numDistinct(self, S, T):
        __ len(S) < len(T):
            return 0
        n = len(S)
        m = len(T)
        t = [0 for i in range(m + 1)]
        t[0] = 1
        for i in range(1, n + 1):
            # j = m ... 1
            for k in range(m):
                j = m - k
                __ S[i - 1] == T[j - 1]:
                    t[j] += t[j - 1]
        return t[m]
