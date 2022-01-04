'''
Created on Mar 4, 2018

@author: tongq
'''
c_ Solution(object):
    ___ countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        s = S
        n = l..(s)
        MOD = 10**9+7
        dp = [[0]*n ___ _ __ r..(n)]
        ___ i __ r..(n):
            dp[i][i] = 1
        ___ l __ r..(1, n):
            ___ i __ r..(n-l):
                j = i+l
                __ s[i] __ s[j]:
                    low = i+1
                    high = j-1
                    w.... low <= high a.. s[low] != s[j]:
                        low += 1
                    w.... low <= high a.. s[high] != s[j]:
                        high -= 1
                    __ low > high:
                        # 'aba'
                        dp[i][j] = dp[i+1][j-1]*2+2
                    ____ low __ high:
                        # 'aaa'
                        dp[i][j] = dp[i+1][j-1]*2+1
                    ____:
                        # 'aacaa'
                        dp[i][j] = dp[i+1][j-1]*2-dp[low+1][high-1]
                ____:
                    dp[i][j] = dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                dp[i][j] = dp[i][j]%MOD
        r.. dp[0][-1]
    
    ___ test
        testCases = [
            'bccb',
            'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = countPalindromicSubsequences(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
