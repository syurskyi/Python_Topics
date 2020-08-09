class Solution:
    # @return an integer
    ___ numDistinct(self, S, T
        __ le.(S) < le.(T
            r_ 0
        n = le.(S)
        m = le.(T)
        t = [0 ___ i in range(m + 1)]
        t[0] = 1
        ___ i in range(1, n + 1
            # j = m ... 1
            ___ k in range(m
                j = m - k
                __ S[i - 1] __ T[j - 1]:
                    t[j] += t[j - 1]
        r_ t[m]
