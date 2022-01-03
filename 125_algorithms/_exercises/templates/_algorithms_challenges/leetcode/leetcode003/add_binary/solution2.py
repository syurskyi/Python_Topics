"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

c_ Solution(object):
    ___ addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        list_a = [int(i) ___ i __ a[::-1]]
        list_b = [int(i) ___ i __ b[::-1]]
        la = l..(list_a)
        lb = l..(list_b)
        # Pad zeroes
        __ la < lb:
            list_a += [0 ___ i __ r..(lb - la)]
            la = l..(list_a)
        ____:
            list_b += [0 ___ i __ r..(la - lb)]
            lb = l..(list_b)
        carry = 0
        res    # list
        ___ i __ r..(la):
            t = (list_a[i] + list_b[i] + carry) % 2
            carry = (list_a[i] + list_b[i] + carry) / 2
            res.a..(t)
        __ carry __ 1:
            res.a..(1)
        r.. ''.j..([s..(d) ___ d __ res[::-1]])
