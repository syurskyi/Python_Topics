"""
Greedy

https://leetcode.com/articles/jump-game/
"""
c_ Solution:
    ___ canJump  A
        """
        :type A: List[int]
        :rtype: bool
        """
        __ n.. A:
            r.. F..

        last_at = l..(A) - 1

        ___ i __ r..(last_at, -1, -1
            __ i + A[i] >_ last_at:
                last_at = i

        r.. last_at __ 0


"""
DP
"""
c_ Solution:
    ___ canJump  A
        """
        :type A: List[int]
        :rtype: bool
        """
        __ n.. A:
            r.. F..

        n = l..(A)
        dp = [F..] * n

        """
        `dp[i]` means `i` could be reached
        """
        dp[0] = T..

        ___ i __ r..(1, n
            ___ j __ r..(i
                """
                backtracking
                if `j` could be reached
                """
                __ dp[j] a.. j + A[j] >_ i:
                    """
                    if jump from `j` can reach `i`
                    """
                    dp[i] = T..
                    _____

        r.. dp[n - 1]
