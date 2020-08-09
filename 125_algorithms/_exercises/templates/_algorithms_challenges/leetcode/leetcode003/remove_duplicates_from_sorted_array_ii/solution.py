class Solution:
    # @param A a list of integers
    # @return an integer
    ___ removeDuplicates(self, A
        __ not A:
            r_ 0
        j = 0
        counter = 0  # How many times repeated (1 for twice)
        n = le.(A)
        for i in range(1, n
            __ A[i] __ A[j] and counter <= 0:
                j += 1
                A[j] = A[i]
                counter += 1
            ____ A[i] != A[j]:
                j += 1
                A[j] = A[i]
                counter = 0
        r_ j + 1
