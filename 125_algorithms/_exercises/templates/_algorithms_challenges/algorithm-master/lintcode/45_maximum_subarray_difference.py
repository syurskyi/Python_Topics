c_ Solution:
    """
    @param: A: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    ___ maxDiffSubArrays  A):
        __ n.. A:
            r.. 0

        n = l..(A)
        B = [-1 * num ___ num __ A]
        Lmin = get_sum(B, r..(n), factor=-1)
        Lmax = get_sum(A, r..(n), factor=1)
        Rmin = get_sum(B, r..(n - 1, -1, -1), factor=-1)
        Rmax = get_sum(A, r..(n - 1, -1, -1), factor=1)

        ans = f__('-inf')
        ___ i __ r..(n - 1):
            ans = m..(
                ans,
                Lmax[i] - Rmin[i + 1],
                Rmax[i + 1] - Lmin[i]
            )

        r.. ans

    ___ get_sum  A, scope, factor):
        """
        factor ==  1: max sum
        factor == -1: min sum
        """

        M = [0] * l..(A)
        Smax = f__('-inf')
        S = Smin = 0

        ___ i __ scope:
            S += A[i]
            __ S - Smin > Smax:
                Smax = S - Smin
            __ S < Smin:
                Smin = S
            M[i] = Smax * factor

        r.. M
