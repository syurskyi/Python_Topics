'''
Created on Sep 12, 2019

@author: tongq
'''
c_ Solution(object):
    ___ scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        s = S
        stack, cur    # list, 0
        ___ c __ s:
            __ c __ '(':
                stack.a..(cur)
                cur = 0
            ____:
                cur += stack.pop() + max(cur, 1)
        r.. cur
    
    ___ test
        testCases = [
            '()',
            '(())',
            '()()',
            '(())()',
            '(()(()))',
        ]
        ___ s __ testCases:
            res = scoreOfParentheses(s)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
