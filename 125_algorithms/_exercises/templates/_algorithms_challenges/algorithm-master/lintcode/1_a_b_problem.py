class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    ___ aplusb(self, a, b
        __ not a:
            r_ b
        __ not b:
            r_ a

        INT_RANGE = 0xFFFFFFFF

        w___ b != 0:
            a, b = a ^ b, (a & b) << 1
            a &= INT_RANGE

        r_ a __ a >> 31 <= 0 else a ^ ~INT_RANGE
