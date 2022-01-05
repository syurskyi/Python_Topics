'''
Created on Feb 12, 2017

@author: MT
'''

c_ Solution(object):
    ___ fractionToDecimal  numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' __ numerator*denominator<0 ____ ''
        result = [sign+s..(n), '.']
        stack    # list
        w.... remainder n.. __ stack:
            stack.a..(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.a..(s..(n))
        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.a..(')')
        r.. ''.j..(result).r..('(0)', '').rstrip('.')
