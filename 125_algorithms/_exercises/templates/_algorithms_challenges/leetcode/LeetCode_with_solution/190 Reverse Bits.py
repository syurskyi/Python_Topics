"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192
(represented in binary as 00111001011110000010100101000000).
"""
__author__ = 'Daniel'


c_ Solution:
    ___ reverseBits  n):
        """
        %2 /2
        """
        ret = 0
        BITS = 32
        ___ i __ xrange(BITS):
            ret += n&1
            __ i __ BITS-1: break
            ret <<= 1
            n >>= 1

        r.. ret
