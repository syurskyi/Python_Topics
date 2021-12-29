class Solution:
    """
    @param A: the arrays
    @return: the number of the intersection of the arrays
    """
    ___ intersectionOfArrays(self, A):
        ans = 0
        __ not A:
            return ans

        n = len(A)
        C = {}

        for i in range(n):
            __ not A[i]:
                return ans

            for a in A[i]:
                __ a not in C:
                    C[a] = set()
                C[a].add(i)

        for a, S in C.items():
            __ len(S) == n:
                ans += 1

        return ans
