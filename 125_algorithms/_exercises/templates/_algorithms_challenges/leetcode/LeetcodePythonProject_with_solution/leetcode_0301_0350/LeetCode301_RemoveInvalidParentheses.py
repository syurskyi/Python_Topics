'''
Created on Mar 11, 2017

@author: MT
'''

c_ Solution(object):
    ___ removeInvalidParentheses(self, s):
        rmL, rmR = 0, 0
        ___ c __ s:
            __ c __ '(':
                rmL += 1
            ____ c __ ')':
                __ rmL > 0:
                    rmL -= 1
                ____:
                    rmR += 1
        result = set()
        helper(s, 0, result, '', rmL, rmR, 0)
        r.. l..(result)
    
    ___ helper(self, s, i, result, elem, rmL, rmR, openNum):
        __ rmL < 0 o. rmR < 0 o. openNum < 0:
            r..
        __ i __ l..(s):
            __ rmL __ 0 a.. rmR __ 0 a.. openNum __ 0:
                result.add(elem)
            r..
        c = s[i]
        __ c __ '(':
            helper(s, i+1, result, elem+c, rmL, rmR, openNum+1)
            helper(s, i+1, result, elem, rmL-1, rmR, openNum)
        ____ c __ ')':
            helper(s, i+1, result, elem+c, rmL, rmR, openNum-1)
            helper(s, i+1, result, elem, rmL, rmR-1, openNum)
        ____:
            helper(s, i+1, result, elem+c, rmL, rmR, openNum)
    
    ___ test
        testCases = [
            '()())()',
            '(a)())()',
            ')(',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = removeInvalidParentheses(s)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ _____ __ _____
    Solution().test()
