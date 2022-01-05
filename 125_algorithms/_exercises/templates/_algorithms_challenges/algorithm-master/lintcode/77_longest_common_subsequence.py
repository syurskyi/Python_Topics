c_ Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: The length of longest common subsequence of A and B
    """
    ___ longestCommonSubsequence  A, B):
        """
        remove the single line comment to print paths
        """
        __ n.. A o. n.. B:
            r.. 0

        m, n = l..(A), l..(B)

        """
        `dp[i][j]` means the size of LCS, consisting of
        the substr end at `A[i - 1]` and the substr end at `B[j - 1]`

        dp[0][j] = 0
        dp[i][0] = 0
        """
        dp = [[0] * (n + 1) ___ _ __ r..(2)]
        # pi = [[0] * (n + 1) for _ in range(m + 1)]

        prev = curr = 0
        ___ i __ r..(1, m + 1):
            prev = curr
            curr = 1 - curr
            ___ j __ r..(1, n + 1):
                """
                case 1: `A[i]` is not one of pairs
                case 2: `B[j]` is not one of pairs
                case 3: `A[i]` and `B[j]` is just a pair
                """
                dp[curr][j] = m..(dp[prev][j], dp[curr][j - 1])

                # if dp[curr][j] == dp[prev][j]:
                #     pi[i][j] = 1
                # else:
                #     pi[i][j] = 2

                __ A[i - 1] __ B[j - 1]:
                    dp[curr][j] = m..(dp[curr][j], dp[prev][j - 1] + 1)

                    # if dp[curr][j] == dp[prev][j - 1] + 1:
                    #     pi[i][j] = 3

        # path = [None] * dp[curr][n]
        # i, j, k = m, n, dp[curr][n] - 1

        # while i > 0 and j > 0:
        #     if pi[i][j] == 1:
        #         i -= 1
        #     elif pi[i][j] == 2:
        #         j -= 1
        #     else:
        #         path[k] = A[i - 1]  # or B[j - 1], its same
        #         k -= 1
        #         i -= 1
        #         j -= 1

        # print(path)

        r.. dp[curr][n]
