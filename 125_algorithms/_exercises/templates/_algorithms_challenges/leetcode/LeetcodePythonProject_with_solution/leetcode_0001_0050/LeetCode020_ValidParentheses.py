'''
Created on Nov 6, 2017

@author: MT
'''
c_ Solution(o..
    ___ isValid  s
        """
        :type s: str
        :rtype: bool
        """
        stack    # list
        ___ c __ s:
            __ c __  '(', '{', ' ' :
                stack.a..(c)
            ____
                __  (c __ ')' a.. stack a.. stack[-1]__'(') o.\
                    (c __ ' ' a.. stack a.. stack[-1]__' ') o.\
                    (c __ '}' a.. stack a.. stack[-1]__'{'
                    stack.p.. )
                ____
                    r.. F..
        r.. stack __ []
    
    ___ test
        testCases = [
            '(){}[]',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = isValid(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
