'''
Created on Nov 6, 2017

@author: MT
'''
class Solution(object):
    ___ isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack    # list
        ___ c __ s:
            __ c __ ['(', '{', '[']:
                stack.a..(c)
            ____:
                __  (c __ ')' a.. stack a.. stack[-1]__'(') o.\
                    (c __ ']' a.. stack a.. stack[-1]__'[') o.\
                    (c __ '}' a.. stack a.. stack[-1]__'{'):
                    stack.pop()
                ____:
                    r.. False
        r.. stack __ []
    
    ___ test(self):
        testCases = [
            '(){}[]',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.isValid(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
