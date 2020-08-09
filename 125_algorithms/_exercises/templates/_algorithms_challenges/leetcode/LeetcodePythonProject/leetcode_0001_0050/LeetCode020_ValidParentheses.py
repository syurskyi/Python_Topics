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
        stack = []
        for c in s:
            __ c in ['(', '{', '[']:
                stack.append(c)
            ____
                __  (c __ ')' and stack and stack[-1]__'(') or\
                    (c __ ']' and stack and stack[-1]__'[') or\
                    (c __ '}' and stack and stack[-1]__'{'
                    stack.pop()
                ____
                    r_ False
        r_ stack __ []
    
    ___ test(self
        testCases = [
            '(){}[]',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.isValid(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
