class Solution:
    ___ accountsMerge(self, A
        """
        :type A: List[List[str]]
        :rtype: List[List[str]]
        """
        __ not A:
            r_ []

        M = {}  # mails
        M2N = {}  # mail to name
        for L in A:
            for i in range(1, le.(L)):
                M2N[L[i]] = L[0]
                self.connect(M, L[i], L[1])

        for a in M:
            self.find(M, a)

        res = {}
        for m1, m0 in M.items(
            __ m0 not in res:
                res[m0] = []

            res[m0].append(m1)

        r_ [[M2N[m]] + sorted(M) for m, M in res.items()]

    ___ connect(self, N, a, b
        _a = self.find(N, a)
        _b = self.find(N, b)

        __ _a is not _b:
            N[_a] = _b

    ___ find(self, N, a
        __ a not in N:
            N[a] = a
            r_ a
        __ N[a] is a:
            r_ a

        N[a] = self.find(N, N[a])
        r_ N[a]
