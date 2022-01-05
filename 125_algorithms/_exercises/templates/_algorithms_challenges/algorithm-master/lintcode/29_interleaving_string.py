c_ Solution:
    """
    @param: A: A string
    @param: B: A string
    @param: C: A string
    @return: Determine whether C is formed by interleaving of A and B
    """
    ___ isInterleave  A, B, C):
        __ A __ N.. o. B __ N.. o. C __ N..
            r.. F..

        __ A __ '' a.. B __ '' a.. C __ '':
            r.. T..

        a, b, c = l..(A), l..(B), l..(C)
        __ c != a + b:
            r.. F..

        """
        `dp[i][j]` means the substr end at `C[i + j - 1]`
        is mixed by the substr end at `A[i - 1]`
        and the substr end at `B[j - 1]`
        """
        dp = [[F..] * (b + 1) ___ _ __ r..(2)]

        prev = curr = 0
        dp[curr][0] = T..

        ___ j __ r..(1, b + 1):
            """
            dp[0][j] = (dp[0][j - 1] and B[j - 1] == C[j - 1])
            """
            __ n.. dp[curr][j - 1]:
                break

            __ B[j - 1] __ C[j - 1]:
                dp[curr][j] = T..

        ___ i __ r..(1, a + 1):
            prev = curr
            curr = 1 - curr

            """
            dp[i][0] = (dp[i - 1][0] and A[i - 1] == C[i - 1])
            """
            __ dp[prev][0] a.. A[i - 1] __ C[i - 1]:
                dp[curr][0] = T..

            ___ j __ r..(1, b + 1):
                dp[curr][j] = F..

                __ dp[prev][j] a.. A[i - 1] __ C[i + j - 1]:
                    dp[curr][j] = T..
                    _____

                __ dp[curr][j - 1] a.. B[j - 1] __ C[i + j - 1]:
                    dp[curr][j] = T..

        r.. dp[curr][b]
