'''
Created on Oct 3, 2017

@author: MT
'''
class Solution(object
    ___ maxA(self, N
        """
        :type N: int
        :rtype: int
        """
        n = N
        dp = [0]*(n+1)
        ___ i __ range(1, n+1
            dp[i] = ma.(dp[i], i)
            ___ j __ range(1, n+1
                __ i+j+2 < n+1:
                    dp[i+j+2] = ma.(dp[i+j+2], dp[i]*(j+1))
        r_ dp[-1]
    
    ___ test(self
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

__  -n __ '__main__':
    Solution().test()
