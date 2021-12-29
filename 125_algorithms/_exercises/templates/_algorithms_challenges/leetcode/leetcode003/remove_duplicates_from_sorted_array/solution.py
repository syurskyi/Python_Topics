class Solution:
    # @param a list of integers
    # @return an integer
    ___ removeDuplicates(self, A):
        __ not A:
            return 0
        __ len(A) == 1:
            return 1
        j = 0  # Position of last processed non-duplicate
        n = len(A)
        for i in range(1, n):
            __ A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1
        return j + 1
