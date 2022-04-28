c_ Solution o..
    ___ numDecodings  s):
        """
        :type s: str
        :rtype: int
        """
        ls = l.. s)
        __ ls __ 0:
            r_ 0
        dp = [0] * ls
        ___ index __ r.. ls):
            __ index >= 1 and int(s[index - 1:index + 1]) < 27 and int(s[index - 1:index + 1]) >= 10:
                __ index __ 1:
                    dp[index] = 1
                ____
                    # 11-26
                    dp[index] += dp[index - 2]
            __ int(s[index]) != 0:
                __ index __ 0:
                    dp[index] = 1
                ____
                    # 1-9
                    dp[index] += dp[index - 1]
        r_ dp[ls - 1]
