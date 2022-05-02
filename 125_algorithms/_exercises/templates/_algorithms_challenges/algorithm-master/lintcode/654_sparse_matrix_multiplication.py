c_ Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    ___ multiply  A, B
        __ n.. A o. n.. B o. l..(A 0 !_ l..(B
            r..    # list

        m, n l..(A), l..(B 0
        l l..(B)

        ans [[0] * n ___ _ __ r..(m)]

        ___ i __ r..(m
            ___ j __ r..(n
                ___ k __ r..(l
                    ans[i][j] += A[i][k] * B[k][j]

        r.. ans
