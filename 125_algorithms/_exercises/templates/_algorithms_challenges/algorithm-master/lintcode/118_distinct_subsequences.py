c_ Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """
    ___ numDistinct  S, T):
        __ S __ N.. o. T __ N..
            r.. 0

        __ S __ '' a.. '':
            r.. 1

        m, n = l..(S), l..(T)

        """
        `dp[i][j]` means the count of distinct subsequences
        (the substr end at `T[j - 1]`) in the substr end at `S[i - 1]`
        """
        dp = [[0] * (n + 1) ___ _ __ r..(2)]

        prev = curr = 0
        dp[curr][0] = 1
        ___ i __ r..(1, m + 1):
            prev = curr
            curr = 1 - curr

            dp[curr][0] = 1

            ___ j __ r..(1, n + 1):
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

        r.. dp[curr][n]
