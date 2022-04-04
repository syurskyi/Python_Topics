"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

__author__ = 'Daniel'


c_ Solution(o..
    ___ getSum  a, b
        """
        circuit full-adder
        since Python don't restrict to 32bit, we need
         1. Masking
         2. Overflow handling
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        MSK = 0xFFFFFFFF

        carry = (a & b) << 1
        out = a ^ b

        # convert to 32 bit
        carry &= MSK
        out &= MSK

        __ carry != 0:
            r.. getSum(out, carry)
        ____
            # handle overflow
            __ out < MAX:
                r.. out
            ____  # negative
                r.. ~(out ^ MSK)