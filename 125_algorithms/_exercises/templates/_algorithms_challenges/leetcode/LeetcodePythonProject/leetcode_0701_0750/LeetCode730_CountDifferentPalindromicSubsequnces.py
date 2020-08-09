'''
Created on Mar 4, 2018

@author: tongq
'''
class Solution(object
    ___ countPalindromicSubsequences(self, S
        """
        :type S: str
        :rtype: int
        """
        s = S
        n = le.(s)
        MOD = 10**9+7
        dp = [[0]*n ___ _ in range(n)]
        ___ i in range(n
            dp[i][i] = 1
        ___ l in range(1, n
            ___ i in range(n-l
                j = i+l
                __ s[i] __ s[j]:
                    low = i+1
                    high = j-1
                    w___ low <= high and s[low] != s[j]:
                        low += 1
                    w___ low <= high and s[high] != s[j]:
                        high -= 1
                    __ low > high:
                        # 'aba'
                        dp[i][j] = dp[i+1][j-1]*2+2
                    ____ low __ high:
                        # 'aaa'
                        dp[i][j] = dp[i+1][j-1]*2+1
                    ____
                        # 'aacaa'
                        dp[i][j] = dp[i+1][j-1]*2-dp[low+1][high-1]
                ____
                    dp[i][j] = dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                dp[i][j] = dp[i][j]%MOD
        r_ dp[0][-1]
    
    ___ test(self
        testCases = [
            'bccb',
            'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.countPalindromicSubsequences(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
