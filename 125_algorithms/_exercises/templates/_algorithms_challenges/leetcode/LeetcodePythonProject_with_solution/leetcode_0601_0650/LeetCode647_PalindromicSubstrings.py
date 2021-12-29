'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object):
    ___ countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ not s: return 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, -1, -1):
                __ s[i] == s[j] and (i-j<=1 or dp[i-1][j+1]):
                    dp[i][j] = True
                    res += 1
        return res
    
    ___ test(self):
        testCases = [
            'abc',
            'aaa',
            'aaaaa',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.countSubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
