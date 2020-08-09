'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object
    ___ countSubstrings(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s: r_ 0
        n = le.(s)
        dp = [[False]*n ___ _ in range(n)]
        res = 0
        ___ i in range(n
            ___ j in range(i, -1, -1
                __ s[i] __ s[j] and (i-j<=1 or dp[i-1][j+1]
                    dp[i][j] = True
                    res += 1
        r_ res
    
    ___ test(self
        testCases = [
            'abc',
            'aaa',
            'aaaaa',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.countSubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
