class Solution:
    ___ findShortestSubArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        __ not A:
            return 0

        n = len(A)
        L, R, C = {}, {}, {}
        for i in range(n):
            __ A[i] not in L:
                L[A[i]] = i
            R[A[i]] = i
            C[A[i]] = C.get(A[i], 0) + 1

        ans = len(A)
        degree = max(C.values())
        for a, c in C.items():
            __ c == degree and R[a] - L[a] + 1 < ans:
                ans = R[a] - L[a] + 1

        return ans
