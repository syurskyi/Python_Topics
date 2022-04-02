'''
Created on Sep 5, 2017

@author: MT
'''

c_ Solution(o..
    ___ isValid  code
        """
        :type code: str
        :rtype: bool
        """
        _______ __
        code = __.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = N..
        w.... code != prev:
            prev = code
            code = __.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        r.. code __ 't'
