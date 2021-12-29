'''
Created on Oct 3, 2017

@author: MT
'''
class Solution(object):
    ___ maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        dp = [0]*(n+1)
        ___ i __ r..(1, n+1):
            dp[i] = max(dp[i], i)
            ___ j __ r..(1, n+1):
                __ i+j+2 < n+1:
                    dp[i+j+2] = max(dp[i+j+2], dp[i]*(j+1))
        r.. dp[-1]
    
    ___ test(self):
        testCases = [
            1,
            2,
            3,
            7,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = self.maxA(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
