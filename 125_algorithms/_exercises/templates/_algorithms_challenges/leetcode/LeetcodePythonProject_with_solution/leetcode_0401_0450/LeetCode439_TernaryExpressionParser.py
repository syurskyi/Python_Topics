'''
Created on Apr 17, 2017

@author: MT
'''

class Solution(object):
    ___ parseTernary(self, expression):
        __ not expression: return ''
        stack = []
        for i in range(len(expression)-1, -1, -1):
            c = expression[i]
            __ stack and stack[-1] == '?':
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                __ c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return stack[-1]
    
    ___ parseTernary_own(self, expression):
        __ len(expression) == 1:
            return expression
        __ expression[0] == 'T':
            subExp = ''
            i = 2
            count = 0
            while i < len(expression):
                __ expression[i] == '?':
                    count += 1
                elif expression[i] == ':':
                    count -= 1
                    __ count == -1:
                        subExp = expression[2:i]
                        break
                i+=1
        else:
            subExp = ''
            i = 2
            count = 0
            while i < len(expression):
                __ expression[i] == '?':
                    count += 1
                elif expression[i] == ':':
                    count -= 1
                    __ count == -1:
                        subExp = expression[i+1:]
                        break
                i+=1
        __ len(subExp) == 1:
            return subExp
        else:
            return self.parseTernary(subExp)
