"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object
    ___ addBinary(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        # a is longer than b
        __ le.(a) < le.(b
            b, a = a, b
        n = le.(a)
        m = le.(b)
        c = 0  # Carry bit
        r = 0  # Result bit
        # i = n - 1 ... 0
        ___ k in range(n
            i = n - 1 - k
            __ k < m:
                j = m - 1 - k
                r = (int(a[i]) + int(b[j]) + c) % 2
                c = (int(a[i]) + int(b[j]) + c) / 2
            ____
                r = (int(a[i]) + c) % 2
                c = (int(a[i]) + c) / 2
            res.insert(0, str(r))
        __ c __ 1:
            res.insert(0, str(c))
        r_ ''.join(res)
