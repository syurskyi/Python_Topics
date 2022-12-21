#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ addBinary  a, b
        """ Recursively binary add.
        """
        __ l..(a) __ 0:
            r_ b
        __ l..(b) __ 0:
            r_ a

        __ a[-1] __ '1' and b[-1] __ '1':
            r_ self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        ____ a[-1] __ '0' and b[-1] __ '0':
            r_ self.addBinary(a[:-1], b[:-1]) + '0'
        ____
            r_ self.addBinary(a[:-1], b[:-1]) + '1'


c.. Solution_2 o..
    ___ addBinary  a, b
        """Iteratively way.
        """
        carry_in, index = '0', 0
        result = ""

        _____ index < m..(l..(a), l..(b)) or carry_in __ '1':
            num_a = a[-1 - index] __ index < l..(a) else '0'
            num_b = b[-1 - index] __ index < l..(b) else '0'

            val = int(num_a) + int(num_b) + int(carry_in)
            result = str(val % 2) + result
            carry_in = '1' __ val > 1 else '0'
            index += 1
        r_ result


c.. Solution_3 o..
    ___ addBinary  a, b
        r_ bin(eval("0b" + a) + eval("0b" + b))[2:]


"""
"0"
"0"
"111000"
"111111111"
"""
