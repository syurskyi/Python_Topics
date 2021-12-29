class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    ___ mergeSortedArray(self, A, B):
        __ not A:
            return B
        __ not B:
            return A

        m, n = len(A), len(B)
        ans = [0] * (m + n)

        i = j = index = 0
        while i < m and j < n:
            __ A[i] < B[j]:
                ans[index] = A[i]
                i += 1
            else:
                ans[index] = B[j]
                j += 1
            index += 1

        while i < m:
            ans[index] = A[i]
            i += 1
            index += 1

        while j < n:
            ans[index] = B[j]
            j += 1
            index += 1

        return ans
