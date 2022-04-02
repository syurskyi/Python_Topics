'''
Created on Apr 17, 2017

@author: MT
'''

c_ Solution(o..
    ___ parseTernary  expression
        __ n.. expression: r.. ''
        stack    # list
        ___ i __ r..(l..(expression)-1, -1, -1
            c = expression[i]
            __ stack a.. stack[-1] __ '?':
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                __ c __ 'T':
                    stack.a..(first)
                ____:
                    stack.a..(second)
            ____:
                stack.a..(c)
        r.. stack[-1]
    
    ___ parseTernary_own  expression
        __ l..(expression) __ 1:
            r.. expression
        __ expression[0] __ 'T':
            subExp = ''
            i = 2
            count = 0
            w.... i < l..(expression
                __ expression[i] __ '?':
                    count += 1
                ____ expression[i] __ ':':
                    count -= 1
                    __ count __ -1:
                        subExp = expression[2:i]
                        _____
                i+=1
        ____:
            subExp = ''
            i = 2
            count = 0
            w.... i < l..(expression
                __ expression[i] __ '?':
                    count += 1
                ____ expression[i] __ ':':
                    count -= 1
                    __ count __ -1:
                        subExp = expression[i+1:]
                        _____
                i+=1
        __ l..(subExp) __ 1:
            r.. subExp
        ____:
            r.. parseTernary(subExp)
