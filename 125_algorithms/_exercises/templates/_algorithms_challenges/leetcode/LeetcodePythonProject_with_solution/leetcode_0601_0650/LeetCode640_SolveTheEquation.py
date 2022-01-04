'''
Created on Sep 27, 2017

@author: MT
'''
c_ Solution(object):
    ___ solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        arr = equation.s..('=')
        s1 = arr[0]
        s2 = arr[1]
        valX1, val1 = solveHelper(s1)
        valX2, val2 = solveHelper(s2)
#         print('valX1, val1: %s, %s' % (valX1, val1))
#         print('valX2, val2: %s, %s' % (valX2, val2))
        __ val1 __ val2:
            __ valX1 __ valX2:
                r.. 'Infinite solutions'
            ____:
                r.. 'x=0'
        ____:
            __ valX1 __ valX2:
                r.. 'No solution'
            ____:
                val = (val2-val1)//(valX1-valX2)
                r.. 'x=%s' % val
    
    ___ solveHelper(self, s):
        valX1, val1 = 0, 0
        i = 0
        w.... i < l..(s):
            __ s[i].isdigit
                sig = 1
                __ i>=1 a.. s[i-1] __ '-':
                    sig = -1
                num = 0
                w.... i < l..(s) a.. s[i].isdigit
                    num = 10*num+i..(s[i])
                    i += 1
                __ i < l..(s) a.. s[i] __ 'x':
                    valX1 += num*sig
                    i += 1
                ____:
                    val1 += num*sig
            ____ s[i] __ 'x':
                __ i __ 0:
                    valX1 += 1
                ____ s[i-1] __ '-':
                    valX1 -= 1
                ____ s[i-1] __ '+':
                    valX1 += 1
            i += 1
        r.. valX1, val1
    
    ___ test
        testCases = [
            'x+5-3+x=6+x-2',
            'x=x',
            '2x=x',
            '2x+3x-6x=x+2',
            'x=x+2',
        ]
        ___ equation __ testCases:
            print('equation: %s' % equation)
            result = solveEquation(equation)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
