# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """

import math

c_ Solution o..
    ___ divide  dividend, divisor):
        __ divisor __ 0:
            r_ MAX_INT
        __ dividend __ 0:
            r_ 0
        isPositive = (dividend < 0) __ (divisor < 0)
        m = abs(dividend)
        n = abs(divisor)
        # ln and exp
        res = math.log(m) - math.log(n)
        res = i..(math.exp(res))
        __ isPositive:
            r_ min(res, 2147483647)
        r_ max(0 - res, -2147483648)

    # def divide(self, dividend, divisor):
    #     # (dividend >= 0) ^ (divisor < 0)
    #     isPositive = (dividend < 0) == (divisor < 0)
    #     dividend, divisor, result = abs(dividend), abs(divisor), 0
    #     while dividend >= divisor:
    #         n, nb = 1, divisor
    #         # fast minus
    #         while dividend >= nb:
    #             dividend, result = dividend - nb, result + n
    #             n, nb = n << 1, nb << 1
    #     if isPositive:
    #         return min(result, 2147483647)
    #     return max(-result, -2147483648)

__ ____ __ ____
    s  ?
    print s.divide(1, 1)


