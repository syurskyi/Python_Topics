c_ Solution:
    ___ findShortestSubArray  A
        """
        :type A: List[int]
        :rtype: int
        """
        __ n.. A:
            r.. 0

        n = l..(A)
        L, R, C    # dict, {}, {}
        ___ i __ r..(n
            __ A[i] n.. __ L:
                L[A[i]] = i
            R[A[i]] = i
            C[A[i]] = C.get(A[i], 0) + 1

        ans = l..(A)
        degree = m..(C.values
        ___ a, c __ C.i..:
            __ c __ degree a.. R[a] - L[a] + 1 < ans:
                ans = R[a] - L[a] + 1

        r.. ans
