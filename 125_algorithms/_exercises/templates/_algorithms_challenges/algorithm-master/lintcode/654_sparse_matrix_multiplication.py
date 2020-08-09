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

        ans = [[0] * n for _ in range(m)]

        for i in range(m
            for j in range(n
                for k in range(l
                    ans[i][j] += A[i][k] * B[k][j]

        r_ ans
