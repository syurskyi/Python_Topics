"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

c_ Solution(o..):
    ___ addBinary  a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res    # list
        # a is longer than b
        __ l..(a) < l..(b):
            b, a = a, b
        n = l..(a)
        m = l..(b)
        c = 0  # Carry bit
        r = 0  # Result bit
        # i = n - 1 ... 0
        ___ k __ r..(n):
            i = n - 1 - k
            __ k < m:
                j = m - 1 - k
                r = (i..(a[i]) + i..(b[j]) + c) % 2
                c = (i..(a[i]) + i..(b[j]) + c) / 2
            ____:
                r = (i..(a[i]) + c) % 2
                c = (i..(a[i]) + c) / 2
            res.insert(0, s..(r))
        __ c __ 1:
            res.insert(0, s..(c))
        r.. ''.j..(res)
