"""
http://www.cnblogs.com/sherylwang/p/5635665.html
"""


class Solution:
    """
    @param: A: A list of integers
    @param: k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    ___ maxSubArray(self, A, k):
        __ n.. A o. n.. k o. l..(A) < k:
            r.. 0

        _INFINITY = float('-inf')
        n = l..(A)

        """
        `G[i][j]` means the global max sum, to pick `j` arrays in [0, i)
        `L[i][j]` means the local max sum, to pick `j` arrays in [0, i),
                  and the `i - 1`th child MUST be included
        """
        G = [[_INFINITY] * (k + 1) ___ _ __ r..(n + 1)]
        L = [[_INFINITY] * (k + 1) ___ _ __ r..(n + 1)]

        ___ i __ r..(n + 1):
            L[i][0] = 0
            G[i][0] = 0

        ___ i __ r..(1, n + 1):
            end = i
            __ k < end:
                end = k
            ___ j __ r..(1, end + 1):
                L[i][j] = A[i - 1] + max(L[i - 1][j], G[i - 1][j - 1])
                G[i][j] = max(L[i][j], G[i - 1][j])

        r.. G[n][k]
