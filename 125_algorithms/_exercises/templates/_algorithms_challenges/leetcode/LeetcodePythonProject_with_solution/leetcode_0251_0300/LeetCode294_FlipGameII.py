'''
Created on Mar 8, 2017

@author: MT
'''

c_ Solution(object):
    ___ canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo    # dict
        r.. helper(s, memo)
    
    ___ helper(self, s, memo):
        __ s __ memo:
            r.. memo[s]
        otherWin = T..
        ___ i __ r..(l..(s)-1):
            __ s[i:i+2] __ '++':
                s0 = s[:i]+'--'+s[i+2:]
                __ n.. helper(s0, memo):
                    otherWin = F..
                    break
        memo[s] = n.. otherWin
        r.. memo[s]
    
    ___ test
        testCases = [
            '++++',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = canWin(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
