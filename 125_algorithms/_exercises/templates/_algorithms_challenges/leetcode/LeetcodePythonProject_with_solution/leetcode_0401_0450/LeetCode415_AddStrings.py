'''
Created on Apr 11, 2017

@author: MT
'''

c_ Solution(o..
    ___ addStrings  num1, num2
        __ l..(num2) > l..(num1
            num1, num2 = num2, num1
        i, j = l..(num1)-1, l..(num2)-1
        result = ''
        carry = 0
        w.... j >_ 0:
            n1 = i..(num1[i])
            n2 = i..(num2[j])
            val = n1+n2+carry
            __ val >_ 10:
                val -= 10
                carry = 1
            ____
                carry = 0
            result = s..(val) + result
            i -= 1
            j -= 1
        w.... i >_ 0:
            n1 = i..(num1[i])
            val = n1+carry
            __ val >_ 10:
                val -= 10
                carry = 1
            ____
                carry = 0
            result = s..(val) + result
            i -= 1
        __ carry:
            result = '1'+result
        r.. result
