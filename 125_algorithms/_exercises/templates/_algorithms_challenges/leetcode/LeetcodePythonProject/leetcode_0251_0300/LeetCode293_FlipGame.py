'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object
    ___ generatePossibleNextMoves(self, s
        result = []
        ___ i in range(1, le.(s)):
            __ s[i-1] __ '+' and s[i] __ '+':
                result.append(s[:i-1]+'--'+s[i+1:])
        r_ result
    
    ___ test(self
        testCases = [
            '++++',
        ]
        ___ s in testCases:
            print('s: %s' % (s))
            result = self.generatePossibleNextMoves(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
