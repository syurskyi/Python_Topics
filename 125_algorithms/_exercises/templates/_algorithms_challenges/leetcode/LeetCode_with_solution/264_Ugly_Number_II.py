c_ Solution o..
    ___ nthUglyNumber  n
        """
        :type n: int
        :rtype: int
        """
        __ n <= 5:
            r_ n
        dp = [0] * (n + 1)
        l1 = l2 = l3 = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        dp[5] = 5
        ___ i __ r.. 6, n + 1
            w.. dp[l1] * 2 <= dp[i - 1]:
                l1 += 1
            w.. dp[l2] * 3 <= dp[i - 1]:
                l2 += 1
            w.. dp[l3] * 5 <= dp[i - 1]:
                l3 += 1
            print l1, l2, l3
            dp[i] = min(dp[l1] * 2, dp[l2] * 3, dp[l3] * 5)
        # print dp
        r_ dp[n]

__ ____ __ ____
    # begin
    s  ?
    print s.nthUglyNumber(10)