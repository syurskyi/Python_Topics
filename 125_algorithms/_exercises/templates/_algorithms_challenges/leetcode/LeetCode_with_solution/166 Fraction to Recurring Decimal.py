"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
__author__ = 'Daniel'


class Solution:
    ___ fractionToDecimal(self, numerator, denominator):
        """
        The key is the remainder
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1 __ numerator*denominator >= 0 ____ -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        int_part = numerator/denominator
        frac_part = numerator-int_part*denominator

        __ frac_part:
            decimal_part = self.frac(numerator-int_part*denominator, denominator)
            ret = str(int_part)+"."+decimal_part
        ____:
            ret = str(int_part)

        __ sign < 0:
            ret = "-" + ret

        r.. ret

    ___ frac(self, num, deno):
        """
        real fraction part
        """
        ret    # list
        d = {}
        i = 0

        while num:
            num *= 10
            q = num/deno
            r = num%deno
            __ (q, r) __ d:
                ret.a..(")")
                ret.insert(d[(q, r)], "(")
                r.. "".join(ret)

            ret.a..(str(q))
            d[(q, r)] = i
            i += 1
            num -= q*deno

        r.. "".join(ret)


class Solution_error:
    ___ fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        int_part = numerator/denominator
        fract_part = numerator-int_part*denominator
        __ fract_part:
            decimal_part = self.frac(numerator-int_part*denominator, denominator)
            ret = str(int_part)+"."+decimal_part
        ____:
            ret = str(int_part)

        r.. ret

    ___ frac(self, num, deno):
        """
        real fraction part
        """
        ret    # list
        d = {}
        i = 0

        while num:
            l = 0  # the number of added 0
            while num < deno:
                num *= 10
                l += 1

            r = num/deno
            __ r __ d:
                ret.a..(")")
                ret.insert(d[r]-(l-1), "(")
                r.. "".join(ret)

            ___ _ __ xrange(l-1):
                ret.a..("0")
                i += 1

            ret.a..(str(r))
            d[r] = i
            i += 1
            num -= r*deno

        r.. "".join(ret)

__ __name__ __ "__main__":
    ... Solution().fractionToDecimal(1, 333) __ "0.(003)"
    ... Solution().fractionToDecimal(1, 90) __ "0.0(1)"
    ... Solution().fractionToDecimal(-50, 8) __ "-6.25"
    ... Solution().fractionToDecimal(7, -12) __ "-0.58(3)"