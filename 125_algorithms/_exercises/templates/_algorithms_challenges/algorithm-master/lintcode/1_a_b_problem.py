class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    ___ aplusb(self, a, b):
        __ n.. a:
            r.. b
        __ n.. b:
            r.. a

        INT_RANGE = 0xFFFFFFFF

        while b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= INT_RANGE

        r.. a __ a >> 31 <= 0 ____ a ^ ~INT_RANGE
