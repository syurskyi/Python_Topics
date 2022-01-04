'''
Created on Feb 22, 2017

@author: MT
'''
c_ Solution(object):
    ___ calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        stack    # list
        sign = 1
        preVal = 0
        w.... i < l..(s):
            __ s[i].isdigit
                preVal = 0
                w.... i < l..(s) a.. s[i].isdigit
                    preVal = preVal*10 + i..(s[i])
                    i += 1
                i -= 1
            ____ s[i] __ '(':
                stack.a..(res)
                stack.a..(sign)
                res = 0
                sign = 1
            ____ s[i] __ ')':
                res += sign*preVal
                res = stack.pop()*res + stack.pop()
                preVal = 0
            ____ s[i] __ '+':
                res += preVal*sign
                sign = 1
            ____ s[i] __ '-':
                res += preVal*sign
                sign = -1
            i += 1
        res += preVal*sign
        r.. res
    
    ___ test
        testCases = [
            '(1+(4+5+2)-3)+(6+8)',
            '(1-3)+(3-5+(3-10)-10)',
            '3+3-1+(3-3)',
            '4312',
            '1+1',
            '2-1 + 2',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = calculate(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
