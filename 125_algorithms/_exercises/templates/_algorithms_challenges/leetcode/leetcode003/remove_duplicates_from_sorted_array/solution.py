class Solution:
    # @param a list of integers
    # @return an integer
    ___ removeDuplicates(self, A
        __ not A:
            r_ 0
        __ le.(A) __ 1:
            r_ 1
        j = 0  # Position of last processed non-duplicate
        n = le.(A)
        ___ i in range(1, n
            __ A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1
        r_ j + 1
