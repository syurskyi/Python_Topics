class Solution:
    # @return an integer
    ___ numDistinct(self, S, T):
        __ l..(S) < l..(T):
            r.. 0
        n = l..(S)
        m = l..(T)
        t = [0 ___ i __ r..(m + 1)]
        t[0] = 1
        ___ i __ r..(1, n + 1):
            # j = m ... 1
            ___ k __ r..(m):
                j = m - k
                __ S[i - 1] __ T[j - 1]:
                    t[j] += t[j - 1]
        r.. t[m]
