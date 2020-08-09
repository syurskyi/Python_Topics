'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object
    ___ canWin(self, s
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        r_ self.helper(s, memo)
    
    ___ helper(self, s, memo
        __ s in memo:
            r_ memo[s]
        otherWin = True
        ___ i in range(le.(s)-1
            __ s[i:i+2] __ '++':
                s0 = s[:i]+'--'+s[i+2:]
                __ not self.helper(s0, memo
                    otherWin = False
                    break
        memo[s] = not otherWin
        r_ memo[s]
    
    ___ test(self
        testCases = [
            '++++',
        ]
        ___ s in testCases:
            print('s: %s' % (s))
            result = self.canWin(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
