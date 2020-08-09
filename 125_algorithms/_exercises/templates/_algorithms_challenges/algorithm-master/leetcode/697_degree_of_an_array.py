class Solution:
    ___ findShortestSubArray(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        __ not A:
            r_ 0

        n = le.(A)
        L, R, C = {}, {}, {}
        ___ i in range(n
            __ A[i] not in L:
                L[A[i]] = i
            R[A[i]] = i
            C[A[i]] = C.get(A[i], 0) + 1

        ans = le.(A)
        degree = max(C.values())
        ___ a, c in C.items(
            __ c __ degree and R[a] - L[a] + 1 < ans:
                ans = R[a] - L[a] + 1

        r_ ans
