c_ Solution:
    # @param S, a string
    # @return an integer
    ___ minCut(self, S):
        __ n.. S:
            r.. -1

        n = l..(S)
        INFINITY = float('inf')
        is_palindrome = get_palin_map(S)

        """
        `dp[i]` means the minimum palindrome count
        broken from the substring ended at `i`
        """
        dp = [INFINITY] * (n + 1)
        dp[0] = 0

        ___ end __ r..(1, n + 1):
            ___ start __ r..(end):
                __ (n.. is_palindrome[start][end - 1] o.
                    dp[start] __ INFINITY):
                    _____
                __ dp[start] + 1 < dp[end]:
                    dp[end] = dp[start] + 1

        r.. dp[n] - 1

    ___ get_palin_map(self, S):
        n = l..(S)
        is_palindrome = [[F..] * n ___ _ __ r..(n)]
        is_palindrome[0][0] = T..

        ___ end __ r..(1, n):
            is_palindrome[end][end] = T..

            start = end - 1
            is_palindrome[start][end] = (S[start] __ S[end])

        ___ start __ r..(n - 1 - 2, -1, -1):
            ___ end __ r..(start + 2, n):
                __ n.. is_palindrome[start + 1][end - 1]:
                    _____
                is_palindrome[start][end] = (S[start] __ S[end])

        r.. is_palindrome
