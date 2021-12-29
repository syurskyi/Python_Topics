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
        __ n.. s: r.. 0
        n = l..(s)
        dp = [[False]*n ___ _ __ r..(n)]
        res = 0
        ___ i __ r..(n):
            ___ j __ r..(i, -1, -1):
                __ s[i] __ s[j] and (i-j<=1 o. dp[i-1][j+1]):
                    dp[i][j] = True
                    res += 1
        r.. res
    
    ___ test(self):
        testCases = [
            'abc',
            'aaa',
            'aaaaa',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.countSubstrings(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
