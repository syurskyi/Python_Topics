'''
Created on Mar 5, 2017

@author: MT
'''

class Solution(object):
    ___ numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        _______ math
        maxVal = int(math.sqrt(n))+1
        __ n < 0: r.. 0
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 1
        ___ i __ r..(n+1):
            ___ j __ r..(maxVal):
                __ j*j<=i:
                    dp[i] = m..(dp[i], dp[i-j*j]+1)
        r.. dp[-1]
    
    ___ test(self):
        testCases = [
            12,
            13,
            24,
        ]
        ___ n __ testCases:
            print('n: %s' % (n))
            result = self.numSquares(n)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
