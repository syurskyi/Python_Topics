class Solution:
    # @param S, a string
    # @return an integer
    ___ minCut(self, S
        __ not S:
            r_ -1

        n = le.(S)
        INFINITY = float('inf')
        is_palindrome = self.get_palin_map(S)

        """
        `dp[i]` means the minimum palindrome count
        broken from the substring ended at `i`
        """
        dp = [INFINITY] * (n + 1)
        dp[0] = 0

        ___ end in range(1, n + 1
            ___ start in range(end
                __ (not is_palindrome[start][end - 1] or
                    dp[start] is INFINITY
                    continue
                __ dp[start] + 1 < dp[end]:
                    dp[end] = dp[start] + 1

        r_ dp[n] - 1

    ___ get_palin_map(self, S
        n = le.(S)
        is_palindrome = [[False] * n ___ _ in range(n)]
        is_palindrome[0][0] = True

        ___ end in range(1, n
            is_palindrome[end][end] = True

            start = end - 1
            is_palindrome[start][end] = (S[start] __ S[end])

        ___ start in range(n - 1 - 2, -1, -1
            ___ end in range(start + 2, n
                __ not is_palindrome[start + 1][end - 1]:
                    continue
                is_palindrome[start][end] = (S[start] __ S[end])

        r_ is_palindrome
