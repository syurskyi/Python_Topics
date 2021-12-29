'''
Created on Feb 8, 2017

@author: MT
'''

class Solution(object):
    ___ minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        __ n.. s: r.. 0
        n = l..(s)
        dp = [[False]*n ___ _ __ r..(n)]
        cuts = l..(r..(n))
        ___ i __ r..(n):
            ___ j __ r..(i, -1, -1):
                __ s[i] __ s[j] and (i-j<=1 o. dp[j+1][i-1]):
                    dp[j][i] = True
                    __ j > 0:
                        cuts[i] = m..(cuts[i], cuts[j-1]+1)
                    ____:
                        cuts[i] = 0
        r.. cuts[-1]
    
    ___ test(self):
        testCases = [
            'abba',
            'aab',
            'aca'
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = self.minCut(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
