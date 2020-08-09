class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    ___ multiply(self, A, B
        __ not A or not B or le.(A[0]) != le.(B
            r_ []

        m, n = le.(A), le.(B[0])
        l = le.(B)

        ans = [[0] * n ___ _ in range(m)]

        ___ i in range(m
            ___ j in range(n
                ___ k in range(l
                    ans[i][j] += A[i][k] * B[k][j]

        r_ ans
