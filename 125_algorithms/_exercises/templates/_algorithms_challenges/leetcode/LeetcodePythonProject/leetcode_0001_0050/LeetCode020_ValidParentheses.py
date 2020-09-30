'''
Created on Nov 6, 2017

@author: MT
'''
class Solution(object
    ___ isValid(self, s
        """
        :type s: str
        :rtype: bool
        """
        stack =   # list
        ___ c __ s:
            __ c __ ['(', '{', '[']:
                stack.append(c)
            ____
                __  (c __ ')' and stack and stack[-1]__'(') or\
                    (c __ ']' and stack and stack[-1]__'[') or\
                    (c __ '}' and stack and stack[-1]__'{'
                    stack.p..
                ____
                    r_ False
        r_ stack __   # list
    
    ___ test(self
        testCases = [
            '(){}[]',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.isValid(s)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
