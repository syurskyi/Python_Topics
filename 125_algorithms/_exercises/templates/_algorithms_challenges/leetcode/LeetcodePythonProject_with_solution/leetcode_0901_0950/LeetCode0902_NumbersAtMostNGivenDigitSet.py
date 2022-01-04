c_ Solution(object):
    ___ atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        s = s..(N)
        k = l..(s)
        dp = [0]*k + [1]
        ___ i __ r..(k-1, -1, -1):
            ___ d __ D:
                __ d < s[i]:
                    dp[i] += l..(D)**(k-i-1)
                ____ d __ s[i]:
                    dp[i] += dp[i+1]
        r.. dp[0] + s..(l..(D)**i ___ i __ r..(1, k))

    ___ test
        testCases = [
            # [["3","4","8"], 4],
            # [['7'], 8],
            # [["1","3","5","7"], 100],
            [["1","4","9"], 1000000000],
        ]
        ___ d, n __ testCases:
            res = atMostNGivenDigitSet(d, n)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
