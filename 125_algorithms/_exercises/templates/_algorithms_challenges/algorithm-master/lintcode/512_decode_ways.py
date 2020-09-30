class Solution:
    """
    @param: s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    ___ numDecodings(self, s
        __ not s or s __ '0':
            r_ 0

        n = le.(s)

        """
        `dp[i]` means the ways to decode

        `dp[0]` => ''
        `dp[1]` => should check if the code is 0
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 __ s[0] __ '0' else 1

        ___ i __ range(2, n + 1
            __ s[i - 1] != '0':
                dp[i] += dp[i - 1]

            __ 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        r_ dp[n]
