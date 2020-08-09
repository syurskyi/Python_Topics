'''
Created on Oct 3, 2017

@author: MT
'''
class Solution(object
    ___ minSteps(self, n
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(2, n+1
            dp[i] = i
            for j in range(i-1, -1, -1
                __ i%j __ 0:
                    dp[i] = dp[j]+i//j
                    break
        r_ dp[-1]
    
    ___ test(self
        testCases = [
            1,
            2,
            3,
            4,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.minSteps(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
