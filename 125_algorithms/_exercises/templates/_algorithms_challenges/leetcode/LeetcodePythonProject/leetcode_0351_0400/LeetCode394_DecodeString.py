'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object
    ___ deconString(self, s
        stack = [['', 1]]
        num = ''
        ___ c in s:
            __ c.isdigit(
                num += c
            ____ c __ '[':
                stack.append(['', int(num)])
                num = ''
            ____ c __ ']':
                st, k = stack.p..
                stack[-1][0] += st*k
            ____
                stack[-1][0] += c
        r_ stack[0][0]
    
    ___ decodeString_own(self, s
        __ '[' not in s:
            r_ s
        result = ''
        i, n = 0, le.(s)
        w___ i < n:
            c = s[i]
            __ c __ '[':
                count = 1
                j = i+1
                w___ j < le.(s) and count > 0:
                    __ s[j] __ '[':
                        count+=1
                    ____ s[j] __ ']':
                        count-=1
                    j+=1
                nextInd = j
                subStr = s[i+1:j-1]
                tmp = self.decodeString(subStr)
                j = i
                w___ j-1 >= 0 and s[j-1].isdigit(
                    j-=1
                times = int(s[j:i])
                result += times*tmp
                i = nextInd
            ____ not c.isdigit(
                result += c
                i += 1
            ____
                i += 1
        r_ result
