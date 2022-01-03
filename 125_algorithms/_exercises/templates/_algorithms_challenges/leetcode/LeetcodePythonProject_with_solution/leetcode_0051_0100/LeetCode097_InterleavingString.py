'''
Created on Jan 30, 2017

@author: MT
'''
c_ Solution(object):
    ___ isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = l..(s1), l..(s2)
        __ m+n != l..(s3):
            r.. F..
        dp = [[F..]*(n+1) ___ _ __ r..(m+1)]
        dp[0][0] = T..
        ___ i __ r..(m):
            __ s1[i] __ s3[i] a.. dp[i][0]:
                dp[i+1][0] = T..
        ___ j __ r..(n):
            __ s2[j] __ s3[j] a.. dp[0][j]:
                dp[0][j+1] = T..
        ___ i __ r..(m):
            ___ j __ r..(n):
                __ s1[i] __ s3[i+j+1] a.. dp[i][j+1]:
                    dp[i+1][j+1] = T..
                __ s2[j] __ s3[i+j+1] a.. dp[i+1][j]:
                    dp[i+1][j+1] = T..
        r.. dp[-1][-1]
    
    ___ test
        testCases = [
            ('aabcc', 'dbbca', 'aadbbcbcac'),
            ('aabcc', 'dbbca', 'aadbbbaccc'),
        ]
        ___ s1, s2, s3 __ testCases:
            print('s1: %s' % (s1))
            print('s2: %s' % (s2))
            print('s3: %s' % (s3))
            result = isInterleave(s1, s2, s3)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()