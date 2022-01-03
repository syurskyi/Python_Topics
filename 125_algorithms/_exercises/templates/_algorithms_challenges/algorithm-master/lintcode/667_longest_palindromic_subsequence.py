c_ Solution:
    """
    @param: s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    ___ longestPalindromeSubseq(self, s):
        __ n.. s:
            r.. 0

        n = l..(s)
        __ n __ 1:
            r.. 1

        # `dp[i][j]` means the length of the longest subsequence
        # included in `s[i:j+1]`
        dp = [[0] * n ___ _ __ r..(n)]

        ans = 0
        start = end = 0
        ___ end __ r..(n):
            dp[end][end] = 1

            __ n < 1:
                continue

            start = end - 1
            __ s[start] __ s[end]:
                dp[start][end] = 2
            ____:
                dp[start][end] = 1

        ___ size __ r..(3, n + 1):
            ___ start __ r..(n - size + 1):
                end = start + size - 1

                dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])

                __ s[start] __ s[end]:
                    dp[start][end] = max(
                        dp[start][end],
                        dp[start + 1][end - 1] + 2
                    )

                __ dp[start][end] > ans:
                    ans = dp[start][end]

        r.. ans
