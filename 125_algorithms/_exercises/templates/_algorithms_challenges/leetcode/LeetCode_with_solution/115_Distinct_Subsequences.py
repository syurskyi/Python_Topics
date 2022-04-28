c_ Solution o..
    ___ numDistinct  s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/51131/space-o-mn-and-o-n-python-solutions
        dp = [[0 ___ j __ xrange(0, l.. t) + 1)] ___ i __ xrange(0, l.. s) + 1)]
        ___ j __ xrange(1, l.. t) + 1):
            dp[0][j] = 0
        ___ i __ xrange(1, l.. s) + 1):
            dp[i][0] = 1
        dp[0][0] = 1
        ___ i __ xrange(1, l.. s) + 1):
            ___ j __ xrange(1, l.. t) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] __ t[j - 1])

        r_ dp[-1][-1]
