'''
Created on Mar 8, 2017

@author: MT
'''

class Solution(object):
    ___ generatePossibleNextMoves(self, s):
        result = []
        for i in range(1, len(s)):
            __ s[i-1] == '+' and s[i] == '+':
                result.append(s[:i-1]+'--'+s[i+1:])
        return result
    
    ___ test(self):
        testCases = [
            '++++',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.generatePossibleNextMoves(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ == '__main__':
    Solution().test()
