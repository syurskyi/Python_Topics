"""
Greedy
"""
c_ Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    ___ jump  A
        __ n.. A:
            r.. -1

        target l..(A) - 1
        start end jumps 0

        w.... end < target:
            jumps += 1
            furthest end
            ___ i __ r..(start, end + 1
                __ i + A[i] > furthest:
                    furthest i + A[i]
            start end + 1
            end furthest

        r.. jumps


"""
DP
"""
c_ Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    ___ jump  A
        __ n.. A:
            r.. -1

        INFINITY f__('inf')

        n l..(A)
        dp [INFINITY] * n
        dp[0] 0

        ___ i __ r..(1, n
            ___ j __ r..(i
                __ (dp[j] < INFINITY a.. j + A[j] >_ i a..
                    dp[j] + 1 < dp[i]
                    dp[i] dp[j] + 1

        r.. dp[n - 1]
