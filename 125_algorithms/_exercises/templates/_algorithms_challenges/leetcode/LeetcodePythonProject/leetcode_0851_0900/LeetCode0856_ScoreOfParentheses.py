'''
Created on Sep 12, 2019

@author: tongq
'''
class Solution(object
    ___ scoreOfParentheses(self, S
        """
        :type S: str
        :rtype: int
        """
        s = S
        stack, cur = [], 0
        ___ c in s:
            __ c __ '(':
                stack.append(cur)
                cur = 0
            ____
                cur += stack.p.. + max(cur, 1)
        r_ cur
    
    ___ test(self
        testCases = [
            '()',
            '(())',
            '()()',
            '(())()',
            '(()(()))',
        ]
        ___ s in testCases:
            res = self.scoreOfParentheses(s)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
