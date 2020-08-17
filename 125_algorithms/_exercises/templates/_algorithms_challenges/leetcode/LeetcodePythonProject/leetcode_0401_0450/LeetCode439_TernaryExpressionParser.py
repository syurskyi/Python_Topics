'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object
    ___ parseTernary(self, expression
        __ not expression: r_ ''
        stack = []
        ___ i in range(le.(expression)-1, -1, -1
            c = expression[i]
            __ stack and stack[-1] __ '?':
                stack.p..
                first = stack.p..
                stack.p..
                second = stack.p..
                __ c __ 'T':
                    stack.append(first)
                ____
                    stack.append(second)
            ____
                stack.append(c)
        r_ stack[-1]
    
    ___ parseTernary_own(self, expression
        __ le.(expression) __ 1:
            r_ expression
        __ expression[0] __ 'T':
            subExp = ''
            i = 2
            count = 0
            w___ i < le.(expression
                __ expression[i] __ '?':
                    count += 1
                ____ expression[i] __ ':':
                    count -= 1
                    __ count __ -1:
                        subExp = expression[2:i]
                        break
                i+=1
        ____
            subExp = ''
            i = 2
            count = 0
            w___ i < le.(expression
                __ expression[i] __ '?':
                    count += 1
                ____ expression[i] __ ':':
                    count -= 1
                    __ count __ -1:
                        subExp = expression[i+1:]
                        break
                i+=1
        __ le.(subExp) __ 1:
            r_ subExp
        ____
            r_ self.parseTernary(subExp)
