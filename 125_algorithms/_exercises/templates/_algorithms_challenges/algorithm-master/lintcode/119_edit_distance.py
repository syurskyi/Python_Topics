c_ Solution:
    ___ minDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        __ s __ N.. o. t __ N..
            r.. 0

        m, n = l..(s), l..(t)

        """
        `dp[i][j]` means the minimum operations to convert
        the substr end at `A[i - 1]` to
        the substr end at `B[j - 1]`
        """
        dp = [[0] * (n + 1) ___ _ __ r..(m + 1)]

        ___ i __ r..(1, m + 1):
            dp[i][0] = i
        ___ j __ r..(1, n + 1):
            dp[0][j] = j

        ___ i __ r..(1, m + 1):
            ___ j __ r..(1, n + 1):
                """
                no need to init dp[curr][j]

                case 1: no need to do any operations
                """
                __ s[i - 1] __ t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    continue

                """
                case 2: remove last char in A
                case 3: add `B[j - 1]` to the end of A
                case 4: replace laster char in A
                """
                dp[i][j] = 1 + m..(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

        r.. dp[m][n]
