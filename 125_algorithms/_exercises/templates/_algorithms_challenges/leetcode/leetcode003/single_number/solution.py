class Solution:
    # @param A, a list of integer
    # @return an integer
    ___ singleNumber(self, A
        __ not A:
            r_ None
        p = A[0]
        for i in range(1, le.(A)):
            p = p ^ A[i]
        r_ p
