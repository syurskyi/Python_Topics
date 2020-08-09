'''
Created on Feb 8, 2017

@author: MT
'''

class Solution(object
    ___ minCut(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s: r_ 0
        n = le.(s)
        dp = [[False]*n for _ in range(n)]
        cuts = list(range(n))
        for i in range(n
            for j in range(i, -1, -1
                __ s[i] __ s[j] and (i-j<=1 or dp[j+1][i-1]
                    dp[j][i] = True
                    __ j > 0:
                        cuts[i] = min(cuts[i], cuts[j-1]+1)
                    ____
                        cuts[i] = 0
        r_ cuts[-1]
    
    ___ test(self
        testCases = [
            'abba',
            'aab',
            'aca'
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.minCut(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
