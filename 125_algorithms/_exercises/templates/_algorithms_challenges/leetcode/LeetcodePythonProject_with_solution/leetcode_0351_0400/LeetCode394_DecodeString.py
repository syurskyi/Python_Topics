'''
Created on Apr 4, 2017

@author: MT
'''

c_ Solution(object):
    ___ deconString(self, s):
        stack = [['', 1]]
        num = ''
        ___ c __ s:
            __ c.isdigit
                num += c
            ____ c __ '[':
                stack.a..(['', i..(num)])
                num = ''
            ____ c __ ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            ____:
                stack[-1][0] += c
        r.. stack[0][0]
    
    ___ decodeString_own(self, s):
        __ '[' n.. __ s:
            r.. s
        result = ''
        i, n = 0, l..(s)
        w.... i < n:
            c = s[i]
            __ c __ '[':
                count = 1
                j = i+1
                w.... j < l..(s) a.. count > 0:
                    __ s[j] __ '[':
                        count+=1
                    ____ s[j] __ ']':
                        count-=1
                    j+=1
                nextInd = j
                subStr = s[i+1:j-1]
                tmp = decodeString(subStr)
                j = i
                w.... j-1 >= 0 a.. s[j-1].isdigit
                    j-=1
                times = i..(s[j:i])
                result += times*tmp
                i = nextInd
            ____ n.. c.isdigit
                result += c
                i += 1
            ____:
                i += 1
        r.. result
