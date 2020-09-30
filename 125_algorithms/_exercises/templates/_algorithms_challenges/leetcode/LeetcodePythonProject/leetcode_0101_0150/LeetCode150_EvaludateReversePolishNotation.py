'''
Created on Feb 11, 2017

@author: MT
'''

class Solution(object
    ___ evalRPN(self, tokens
        """
        :type tokens: List[str]
        :rtype: int
        """
        ______ operator
        stack =   # list
        ___ token __ tokens:
            __ token __ '+':
                num1 = stack.p..
                num2 = stack.p..
                stack.append(num1+num2)
            ____ token __ '-':
                num1 = stack.p..
                num2 = stack.p..
                stack.append(num2-num1)
            ____ token __ '*':
                num1 = stack.p..
                num2 = stack.p..
                stack.append(num1*num2)
            ____ token __ '/':
                num1 = stack.p..
                num2 = stack.p..
                stack.append(int(operator.truediv(num2, num1) ))
            ____
                stack.append(int(token))
        r_ stack[-1]
    
    ___ test(self
        testCases = [
#             ["2", "1", "+", "3", "*"],
#             ["4", "13", "5", "/", "+"],
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        ]
        ___ tokens __ testCases:
            print('tokens: %s' % (tokens))
            result = self.evalRPN(tokens)
            print('result: %s' % (result))
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()