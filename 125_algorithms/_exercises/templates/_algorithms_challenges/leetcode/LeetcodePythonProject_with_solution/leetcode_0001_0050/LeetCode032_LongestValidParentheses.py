'''
Created on Mar 14, 2017

@author: MT
'''

c_ Solution(o..
    ___ longestValidParentheses  s
        left = -1
        stack    # list
        res = 0
        ___ i, c __ e..(s
            __ c __ '(':
                stack.a..(i)
            ____:
                __ stack:
                    stack.pop()
                    __ stack:
                        res = m..(res, i-stack[-1])
                    ____:
                        res = m..(res, i-left)
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

__ _____ __ _____
    Solution().test()
