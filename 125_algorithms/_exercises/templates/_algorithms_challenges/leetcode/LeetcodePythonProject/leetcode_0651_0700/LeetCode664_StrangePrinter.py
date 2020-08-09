'''
Created on Oct 9, 2017

@author: MT
'''
class Solution(object
    ___ strangePrinter(self, s
        """
        :type s: str
        :rtype: int
        """
        __ not s: r_ 0
        n = le.(s)
        dp = [[0]*n ___ _ in range(n)]
        ___ i in range(n
            dp[i][i] = 1
        ___ i in range(1, n
            ___ j in range(n-i
                dp[j][j+i] = i+1
                ___ k in range(j+1, j+i+1
                    tmp = dp[j][k-1]+dp[k][j+i]
                    __ s[k-1] __ s[j+i]:
                        tmp -= 1
                    dp[j][j+i] = min(dp[j][j+i], tmp)
        r_ dp[0][n-1]
    
    ___ test(self
        testCases = [
            'aaabbb',
            'aba',
            'abcabc',
        ]
        ___ s in testCases:
            print('s: %s' % s)
            result = self.strangePrinter(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
