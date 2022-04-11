'''
Created on Sep 12, 2019

@author: tongq
'''
c_ Solution(o..
    ___ scoreOfParentheses  S
        """
        :type S: str
        :rtype: int
        """
        s S
        stack, cur    # list, 0
        ___ c __ s:
            __ c __ '(':
                stack.a..(cur)
                cur 0
            ____
                cur += stack.p.. ) + m..(cur, 1)
        r.. cur
    
    ___ test
        testCases [
            '()',
            '(())',
            '()()',
            '(())()',
            '(()(()))',
        ]
        ___ s __ testCases:
            res scoreOfParentheses(s)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
