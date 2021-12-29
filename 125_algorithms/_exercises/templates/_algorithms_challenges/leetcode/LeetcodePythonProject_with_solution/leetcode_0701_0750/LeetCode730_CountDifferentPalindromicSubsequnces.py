'''
Created on Mar 4, 2018

@author: tongq
'''
class Solution(object):
    ___ countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        s = S
        n = len(s)
        MOD = 10**9+7
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                __ s[i] == s[j]:
                    low = i+1
                    high = j-1
                    while low <= high and s[low] != s[j]:
                        low += 1
                    while low <= high and s[high] != s[j]:
                        high -= 1
                    __ low > high:
                        # 'aba'
                        dp[i][j] = dp[i+1][j-1]*2+2
                    elif low == high:
                        # 'aaa'
                        dp[i][j] = dp[i+1][j-1]*2+1
                    else:
                        # 'aacaa'
                        dp[i][j] = dp[i+1][j-1]*2-dp[low+1][high-1]
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
                dp[i][j] = dp[i][j]%MOD
        return dp[0][-1]
    
    ___ test(self):
        testCases = [
            'bccb',
            'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.countPalindromicSubsequences(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
