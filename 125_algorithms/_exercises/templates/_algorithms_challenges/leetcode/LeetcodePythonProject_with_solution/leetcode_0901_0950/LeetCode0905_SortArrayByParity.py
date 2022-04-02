c_ Solution(o..
    ___ sortArrayByParity  A
        """
        :type A: List[int]
        :rtype: List[int]
        """
        __ n.. A: r.. A
        i, j = 0, l..(A)-1
        w.... i < j:
            w.... i < j a.. A[i] % 2 __ 0:
                i += 1
            w.... i < j a.. A[j] % 2 __ 1:
                j -= 1
            __ i < j:
                A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        r.. A
