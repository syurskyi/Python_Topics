'''
Created on Mar 11, 2017

@author: MT
'''

class Solution(object
    ___ removeInvalidParentheses(self, s
        rmL, rmR = 0, 0
        ___ c in s:
            __ c __ '(':
                rmL += 1
            ____ c __ ')':
                __ rmL > 0:
                    rmL -= 1
                ____
                    rmR += 1
        result = set()
        self.helper(s, 0, result, '', rmL, rmR, 0)
        r_ list(result)
    
    ___ helper(self, s, i, result, elem, rmL, rmR, openNum
        __ rmL < 0 or rmR < 0 or openNum < 0:
            r_
        __ i __ le.(s
            __ rmL __ 0 and rmR __ 0 and openNum __ 0:
                result.add(elem)
            r_
        c = s[i]
        __ c __ '(':
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum+1)
            self.helper(s, i+1, result, elem, rmL-1, rmR, openNum)
        ____ c __ ')':
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum-1)
            self.helper(s, i+1, result, elem, rmL, rmR-1, openNum)
        ____
            self.helper(s, i+1, result, elem+c, rmL, rmR, openNum)
    
    ___ test(self
        testCases = [
            '()())()',
            '(a)())()',
            ')(',
        ]
        ___ s in testCases:
            print('s: %s' % (s))
            result = self.removeInvalidParentheses(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
