'''
Created on Mar 14, 2017

@author: MT
'''

c_ Solution(object):
    ___ longestValidParentheses(self, s):
        left = -1
        stack    # list
        res = 0
        ___ i, c __ e..(s):
            __ c __ '(':
                stack.a..(i)
            ____:
                __ stack:
                    stack.pop()
                    __ stack:
                        res = max(res, i-stack[-1])
                    ____:
                        res = max(res, i-left)
                ____:
                    left = i
        r.. res
    
    ___ test
        testCases = [
            '()',
            '(()',
            ')()())',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = longestValidParentheses(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
