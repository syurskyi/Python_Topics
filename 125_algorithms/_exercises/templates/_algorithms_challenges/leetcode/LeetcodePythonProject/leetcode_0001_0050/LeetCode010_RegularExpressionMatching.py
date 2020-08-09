'''
Created on May 5, 2017

@author: MT
'''
class Solution(object
    ___ isMatch(self, s, p
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = le.(s), le.(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(n
            __ p[j] __ '*' and dp[0][j-1]:
                dp[0][j+1] = True
        for i in range(m
            for j in range(n
                __ s[i] __ p[j] or p[j] __ '.':
                    dp[i+1][j+1] = dp[i][j]
                ____ p[j] __ '*':
                    __ p[j-1] __ '.' or s[i] __ p[j-1]:
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j-1]
                    ____
                        dp[i+1][j+1] = dp[i+1][j-1]
        r_ dp[-1][-1]
    
    ___ test(self
        testCases = [
            ['aa', 'a'],
            ['aa', 'a*'],
            ['ab', '.*'],
            ['aab', 'c*a*b'],
            ['mississippi', 'mis*is*p*.'],
        ]
        for s, p in testCases:
            print('s: %s' % s)
            print('p: %s' % p)
            result = self.isMatch(s, p)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
