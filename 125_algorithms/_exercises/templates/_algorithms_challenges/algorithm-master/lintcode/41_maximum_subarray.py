"""
Prefix Sum: space optimization
"""
c_ Solution:
    """
    @param: A: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    ___ maxSubArray  A
        """
        the answer is the maximum segment sum,
        that is, `S[i] - Smin`
        """
        __ n.. A:
            r.. 0

        ans = f__('-inf')
        S = Smin = 0
        ___ i __ r..(l..(A:
            S += A[i]

            __ S - Smin > ans:
                ans = S - Smin

            """
            since the sum of [i, j] in A is `S[j] - S[i - 1]`
            so we need to find the `Smin` at the end of iteration
            """
            __ S < Smin:
                Smin = S

        r.. ans


"""
Prefix Sum
"""
c_ Solution:
    """
    @param: A: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    ___ maxSubArray  A
        """
        the answer is the maximum segment sum,
        that is, `S[i] - Smin`
        """
        __ n.. A:
            r.. 0

        n = l..(A)
        ans = f__('-inf')

        Smin = 0
        S = [0] * (n + 1)
        ___ i __ r..(1, n + 1
            S[i] = S[i - 1] + A[i - 1]

            __ S[i] - Smin > ans:
                ans = S[i] - Smin

            """
            since the sum of [i, j] in A is `S[j] - S[i - 1]`
            so we need to find the `Smin` at the end of iteration
            """
            __ S[i] < Smin:
                Smin = S[i]

        r.. ans
