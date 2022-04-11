c_ Solution:
    ___ accountsMerge  A
        """
        :type A: List[List[str]]
        :rtype: List[List[str]]
        """
        __ n.. A:
            r.. []

        M    # dict  # mails
        M2N    # dict  # mail to name
        ___ L __ A:
            ___ i __ r..(1, l..(L:
                M2N[L[i]] L[0]
                connect(M, L[i], L[1])

        ___ a __ M:
            find(M, a)

        res    # dict
        ___ m1, m0 __ M.i..:
            __ m0 n.. __ res:
                res[m0]    # list

            res[m0].a..(m1)

        r.. [[M2N[m]] + s..(M) ___ m, M __ res.i..]

    ___ connect  N, a, b
        _a find(N, a)
        _b find(N, b)

        __ _a __ n.. _b:
            N[_a] _b

    ___ find  N, a
        __ a n.. __ N:
            N[a] a
            r.. a
        __ N[a] __ a:
            r.. a

        N[a] find(N, N[a])
        r.. N[a]
