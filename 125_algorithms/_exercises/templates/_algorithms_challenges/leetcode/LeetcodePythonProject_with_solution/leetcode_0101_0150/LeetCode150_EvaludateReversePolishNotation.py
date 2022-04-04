'''
Created on Feb 11, 2017

@author: MT
'''

c_ Solution(o..
    ___ evalRPN  tokens
        """
        :type tokens: List[str]
        :rtype: int
        """
        _______ operator
        stack    # list
        ___ token __ tokens:
            __ token __ '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.a..(num1+num2)
            ____ token __ '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.a..(num2-num1)
            ____ token __ '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.a..(num1*num2)
            ____ token __ '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.a..(i..(operator.truediv(num2, num1)
            ____:
                stack.a..(i..(token
        r.. stack[-1]
    
    ___ test
        testCases = [
#             ["2", "1", "+", "3", "*"],
#             ["4", "13", "5", "/", "+"],
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        ]
        ___ tokens __ testCases:
            print('tokens: %s' % (tokens
            result = evalRPN(tokens)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()