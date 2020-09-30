class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    ___ multiply(self, A, B
        __ not A or not B or le.(A[0]) != le.(B
            r_   # list

        m, n = le.(A), le.(B[0])
        l = le.(B)

        ans = [[0] * n ___ _ __ range(m)]

        ___ i __ range(m
            ___ j __ range(n
                ___ k __ range(l
                    ans[i][j] += A[i][k] * B[k][j]

        r_ ans
