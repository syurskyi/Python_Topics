'''
Created on Jan 30, 2017

@author: MT
'''
class Solution(object):
    ___ isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        __ m+n != len(s3):
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m):
            __ s1[i] == s3[i] and dp[i][0]:
                dp[i+1][0] = True
        for j in range(n):
            __ s2[j] == s3[j] and dp[0][j]:
                dp[0][j+1] = True
        for i in range(m):
            for j in range(n):
                __ s1[i] == s3[i+j+1] and dp[i][j+1]:
                    dp[i+1][j+1] = True
                __ s2[j] == s3[i+j+1] and dp[i+1][j]:
                    dp[i+1][j+1] = True
        return dp[-1][-1]
    
    ___ test(self):
        testCases = [
            ('aabcc', 'dbbca', 'aadbbcbcac'),
            ('aabcc', 'dbbca', 'aadbbbaccc'),
        ]
        for s1, s2, s3 in testCases:
            print('s1: %s' % (s1))
            print('s2: %s' % (s2))
            print('s3: %s' % (s3))
            result = self.isInterleave(s1, s2, s3)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()