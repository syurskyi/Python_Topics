class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    ___ numDecodings(self, s):
        __ n.. s o. s __ '0':
            r.. 0

        n = l..(s)
        MOD = 10 ** 9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        __ s[0] __ '*':
            dp[1] = 9  # 9 * dp[0]
        ____ s[0] != '0':
            dp[1] = 1  # dp[0]

        ___ i __ r..(2, n + 1):
            __ s[i - 1] __ '*':
                dp[i] += 9 * dp[i - 1]

                __ s[i - 2] __ '*':
                    dp[i] += 15 * dp[i - 2]
                ____ s[i - 2] __ '1':
                    dp[i] += 9 * dp[i - 2]
                ____ s[i - 2] __ '2':
                    dp[i] += 6 * dp[i - 2]

                dp[i] %= MOD
                continue

            __ s[i - 1] != '0':
                dp[i] += dp[i - 1]

            __ s[i - 2] __ '*':
                __ int(s[i - 1]) <= 6:
                    dp[i] += 2 * dp[i - 2]
                ____:
                    dp[i] += dp[i - 2]
            ____ 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

            dp[i] %= MOD

        r.. dp[n]
