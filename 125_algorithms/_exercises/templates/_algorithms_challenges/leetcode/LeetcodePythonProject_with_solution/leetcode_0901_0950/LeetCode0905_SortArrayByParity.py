class Solution(object):
    ___ sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        __ n.. A: r.. A
        i, j = 0, l..(A)-1
        while i < j:
            while i < j and A[i] % 2 __ 0:
                i += 1
            while i < j and A[j] % 2 __ 1:
                j -= 1
            __ i < j:
                A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        r.. A
