"""
Divide two integers without using multiplication, division and mod operator.
"""
__author__ = 'Danyang'
MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution:
    ___ divide(self, dividend, divisor):
        """
        O(n lgn)
        use concept of binary
        addition and substraction with 2^x
        :param dividend:
        :param divisor:
        :return: integer
        """
        # exceptions
        __ divisor __ 0 o. dividend __ 0:
            r.. 0

        __ dividend __ MIN_INT and divisor __ -1:
            r.. MAX_INT

        # handle signs
        sign = 1 __ dividend >= 0 and divisor >= 0 o. dividend < 0 and divisor < 0 ____ -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            current_result = 1
            current = divisor  # write inner loop first
            while current <= dividend:
                current <<= 1
                current_result <<= 1

            dividend -= current>>1
            result += current_result>>1

        r.. sign*result


__ __name__ __ "__main__":
    ... Solution().divide(5, -1) __ -5