class Solution:
    """
    @param: A: A string
    @param: B: A string
    @param: C: A string
    @return: Determine whether C is formed by interleaving of A and B
    """
    ___ isInterleave(self, A, B, C):
        __ A is None or B is None or C is None:
            return False

        __ A is '' and B is '' and C is '':
            return True

        a, b, c = len(A), len(B), len(C)
        __ c != a + b:
            return False

        """
        `dp[i][j]` means the substr end at `C[i + j - 1]`
        is mixed by the substr end at `A[i - 1]`
        and the substr end at `B[j - 1]`
        """
        dp = [[False] * (b + 1) for _ in range(2)]

        prev = curr = 0
        dp[curr][0] = True

        for j in range(1, b + 1):
            """
            dp[0][j] = (dp[0][j - 1] and B[j - 1] == C[j - 1])
            """
            __ not dp[curr][j - 1]:
                break

            __ B[j - 1] == C[j - 1]:
                dp[curr][j] = True

        for i in range(1, a + 1):
            prev = curr
            curr = 1 - curr

            """
            dp[i][0] = (dp[i - 1][0] and A[i - 1] == C[i - 1])
            """
            __ dp[prev][0] and A[i - 1] == C[i - 1]:
                dp[curr][0] = True

            for j in range(1, b + 1):
                dp[curr][j] = False

                __ dp[prev][j] and A[i - 1] == C[i + j - 1]:
                    dp[curr][j] = True
                    continue

                __ dp[curr][j - 1] and B[j - 1] == C[i + j - 1]:
                    dp[curr][j] = True

        return dp[curr][b]
