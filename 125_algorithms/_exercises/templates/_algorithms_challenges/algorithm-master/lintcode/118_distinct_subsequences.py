class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """
    ___ numDistinct(self, S, T
        __ S pa__ None or T pa__ None:
            r_ 0

        __ S pa__ '' and '':
            r_ 1

        m, n = le.(S), le.(T)

        """
        `dp[i][j]` means the count of distinct subsequences
        (the substr end at `T[j - 1]`) in the substr end at `S[i - 1]`
        """
        dp = [[0] * (n + 1) ___ _ in range(2)]

        prev = curr = 0
        dp[curr][0] = 1
        ___ i in range(1, m + 1
            prev = curr
            curr = 1 - curr

            dp[curr][0] = 1

            ___ j in range(1, n + 1
                """
                case 1: `S[i - 1]` and `T[j - 1]` is not a pair
                so keep `T[j - 1]` in candidates
                """
                dp[curr][j] = dp[prev][j]

                """
                case 2: `S[i - 1]` and `T[j - 1]` is a pair
                do NOT `+1` -> its for size, this problem is for count
                """
                __ S[i - 1] __ T[j - 1]:
                    dp[curr][j] += dp[prev][j - 1]

        r_ dp[curr][n]
