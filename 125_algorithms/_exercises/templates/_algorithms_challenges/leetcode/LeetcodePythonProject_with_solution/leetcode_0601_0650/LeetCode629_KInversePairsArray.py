'''
Created on Sep 10, 2017

@author: MT
'''
c_ Solution(object):
    ___ kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10**9+7
        __ k > n*(n-1)//2 o. k < 0:
            r.. 0
        __ k __ 0 o. k __ n*(n-1)//2:
            r.. 1
        dp = [[0]*(k+1) ___ _ __ r..(n+1)]
        dp[2][0] = 1
        dp[2][1] = 1
        ___ i __ r..(3, n+1):
            dp[i][0] = 1
            ___ j __ r..(1, m..(k, i*(i-1)//2)+1):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
                __ j >= i:
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] = (dp[i][j]+mod)%mod
        r.. dp[-1][-1]
    
    ___ kInversePairs_another(self, n, k):
        mod = 10**9+7
        dp = [0]+[1]*(k+1)
        ___ i __ r..(2, n+1):
            new = [0]
            ___ j __ r..(k+1):
                v = dp[j+1]
                __ j >= i:
                    v -= dp[j-i+1]
                new.a..((new[-1]+v)%mod)
            dp = new
        r.. (dp[k+1]-dp[k])%mod
    
    ___ test
        testCases = [
            (3, 0),
            (3, 1),
            (3, 2),
        ]
        ___ n, k __ testCases:
            print('n: %s' % n)
            print('k: %s' % k)
            result = kInversePairs(n, k)
            print('result: %s' % result)
            result2 = kInversePairs_another(n, k)
            print('result2: %s' % result2)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
