'''
Created on Apr 17, 2018

@author: tongq
'''
class Solution(object):
    ___ preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        dp = [0]*13
        dp[0] = 1
        ___ i __ r..(1, 13):
            dp[i] = dp[i-1]*5+1
        ___ i __ r..(12, -1, -1):
            __ K//dp[i] __ 5:
                r.. 0
            K = K%dp[i]
        r.. 5
    
    ___ test(self):
        testCases = [
            0,
            5,
        ]
        ___ k __ testCases:
            print('k: %s' % k)
            result = self.preimageSizeFZF(k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
