class Solution:
    # @param A, a list of integer
    # @return an integer
    ___ singleNumber(self, A):
        __ not A:
            return None
        p = A[0]
        for i in range(1, len(A)):
            p = p ^ A[i]
        return p
