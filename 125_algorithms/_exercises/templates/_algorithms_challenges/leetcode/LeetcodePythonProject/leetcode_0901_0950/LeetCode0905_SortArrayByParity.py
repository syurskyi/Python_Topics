class Solution(object
    ___ sortArrayByParity(self, A
        """
        :type A: List[int]
        :rtype: List[int]
        """
        __ not A: r_ A
        i, j = 0, le.(A)-1
        w___ i < j:
            w___ i < j and A[i] % 2 __ 0:
                i += 1
            w___ i < j and A[j] % 2 __ 1:
                j -= 1
            __ i < j:
                A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        r_ A
