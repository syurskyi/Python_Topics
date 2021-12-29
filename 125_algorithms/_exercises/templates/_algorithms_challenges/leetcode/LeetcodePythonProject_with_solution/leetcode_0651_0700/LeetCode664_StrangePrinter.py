'''
Created on Oct 9, 2017

@author: MT
'''
class Solution(object):
    ___ strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        n = l..(s)
        dp = [[0]*n ___ _ __ r..(n)]
        ___ i __ r..(n):
            dp[i][i] = 1
        ___ i __ r..(1, n):
            ___ j __ r..(n-i):
                dp[j][j+i] = i+1
                ___ k __ r..(j+1, j+i+1):
                    tmp = dp[j][k-1]+dp[k][j+i]
                    __ s[k-1] __ s[j+i]:
                        tmp -= 1
                    dp[j][j+i] = m..(dp[j][j+i], tmp)
        r.. dp[0][n-1]
    
    ___ test(self):
        testCases = [
            'aaabbb',
            'aba',
            'abcabc',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.strangePrinter(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
