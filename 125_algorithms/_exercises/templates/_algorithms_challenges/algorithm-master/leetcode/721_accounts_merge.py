class Solution:
    ___ accountsMerge(self, A):
        """
        :type A: List[List[str]]
        :rtype: List[List[str]]
        """
        __ n.. A:
            r.. []

        M = {}  # mails
        M2N = {}  # mail to name
        ___ L __ A:
            ___ i __ r..(1, l..(L)):
                M2N[L[i]] = L[0]
                self.connect(M, L[i], L[1])

        ___ a __ M:
            self.find(M, a)

        res = {}
        ___ m1, m0 __ M.items():
            __ m0 n.. __ res:
                res[m0]    # list

            res[m0].a..(m1)

        r.. [[M2N[m]] + s..(M) ___ m, M __ res.items()]

    ___ connect(self, N, a, b):
        _a = self.find(N, a)
        _b = self.find(N, b)

        __ _a __ n.. _b:
            N[_a] = _b

    ___ find(self, N, a):
        __ a n.. __ N:
            N[a] = a
            r.. a
        __ N[a] __ a:
            r.. a

        N[a] = self.find(N, N[a])
        r.. N[a]
