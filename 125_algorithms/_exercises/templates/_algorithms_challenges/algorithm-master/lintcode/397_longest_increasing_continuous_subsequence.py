"""
DP + print path
remove the single line comment to see the path in result
"""
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    ___ longestIncreasingContinuousSubsequence(self, A
        __ not A:
            r_ 0

        size = self.get_lics_size(A)
        A.reverse()
        _size = self.get_lics_size(A)

        r_ max(size, _size)

    ___ get_lics_size(self, A
        ans = 0
        n = le.(A)

        """
        `dp[i]` means the size of LICS ended at `A[i]`
        note that there is size, so init with `1`
        """
        dp = [1] * n

        # pi = [-1] * n
        # end_at = -1

        for i in range(n
            __ i > 0 and A[i] > A[i - 1]:
                dp[i] = dp[i - 1] + 1
                # pi[i] = i - 1
            __ dp[i] > ans:
                ans = dp[i]
                # end_at = i

        # paths = [0] * ans
        # for i in range(ans - 1, -1, -1
        #     paths[i] = A[end_at]
        #     end_at = pi[end_at]
        # print(paths)

        r_ ans


"""
Optimized
"""
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    ___ longestIncreasingContinuousSubsequence(self, A
        __ not A:
            r_ 0

        size = self.get_lics_size(A)
        A.reverse()
        _size = self.get_lics_size(A)

        r_ max(size, _size)

    ___ get_lics_size(self, A
        ans = size = 1

        for i in range(1, le.(A)):
            __ A[i] > A[i - 1]:
                size += 1
            ____
                size = 1

            __ size > ans:
                ans = size

        r_ ans
