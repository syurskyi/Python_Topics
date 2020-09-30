'''
Created on Mar 14, 2017

@author: MT
'''

class Solution(object
    ___ longestValidParentheses(self, s
        left = -1
        stack =   # list
        res = 0
        ___ i, c __ enumerate(s
            __ c __ '(':
                stack.append(i)
            ____
                __ stack:
                    stack.p..
                    __ stack:
                        res = ma.(res, i-stack[-1])
                    ____
                        res = ma.(res, i-left)
                ____
                    left = i
        r_ res
    
    ___ test(self
        testCases = [
            '()',
            '(()',
            ')()())',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.longestValidParentheses(s)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
