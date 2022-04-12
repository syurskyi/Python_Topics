"""
Given two numbers represented as strings, return multiplication of the numbers
as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""


c_ Solution(o..
    ___ multiply  num1, num2
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a num1[::-1]
        b num2[::-1]
        n l..(a)
        m l..(b)
        res =  '0' ___ i __ r..(n + m)]
        ___ i __ r..(n
            c 0
            ___ j __ r..(m
                tmp  i..(a[i]) * i..(b[j]) + i..(res[i + j]) + c
                digit tmp % 10
                res[i + j] s..(digit)
                c tmp / 10
            __ c > 0:
                res[m + i] s..(c)
        res ''.j..(res[::-1])
        ___ i, d __ e..(res
            __ d !_ '0':
                r.. res[i:]
        ____
            r.. '0'

s Solution()

print s.multiply('2', '21')
print s.multiply('83', '3')
