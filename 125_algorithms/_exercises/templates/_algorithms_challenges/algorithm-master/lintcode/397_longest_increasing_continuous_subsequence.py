"""
DP + print path
remove the single line comment to see the path in result
"""
c_ Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    ___ longestIncreasingContinuousSubsequence  A
        __ n.. A:
            r.. 0

        size = get_lics_size(A)
        A.r..
        _size = get_lics_size(A)

        r.. m..(size, _size)

    ___ get_lics_size  A
        ans = 0
        n = l..(A)

        """
        `dp[i]` means the size of LICS ended at `A[i]`
        note that there is size, so init with `1`
        """
        dp = [1] * n

        # pi = [-1] * n
        # end_at = -1

        ___ i __ r..(n
            __ i > 0 a.. A[i] > A[i - 1]:
                dp[i] = dp[i - 1] + 1
                # pi[i] = i - 1
            __ dp[i] > ans:
                ans = dp[i]
                # end_at = i

        # paths = [0] * ans
        # for i in range(ans - 1, -1, -1):
        #     paths[i] = A[end_at]
        #     end_at = pi[end_at]
        # print(paths)

        r.. ans


"""
Optimized
"""
c_ Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    ___ longestIncreasingContinuousSubsequence  A
        __ n.. A:
            r.. 0

        size = get_lics_size(A)
        A.r..
        _size = get_lics_size(A)

        r.. m..(size, _size)

    ___ get_lics_size  A
        ans = size = 1

        ___ i __ r..(1, l..(A:
            __ A[i] > A[i - 1]:
                size += 1
            ____:
                size = 1

            __ size > ans:
                ans = size

        r.. ans
