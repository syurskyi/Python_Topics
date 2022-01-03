'''
Created on Oct 3, 2017

@author: MT
'''
c_ Solution(object):
    ___ minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        ___ i __ r..(2, n+1):
            dp[i] = i
            ___ j __ r..(i-1, -1, -1):
                __ i%j __ 0:
                    dp[i] = dp[j]+i//j
                    break
        r.. dp[-1]
    
    ___ test
        testCases = [
            1,
            2,
            3,
            4,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = minSteps(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
