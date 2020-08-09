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
    ___ fractionToDecimal(self, numerator, denominator
        """
        The key is the remainder
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1 __ numerator*denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        int_part = numerator/denominator
        frac_part = numerator-int_part*denominator

        __ frac_part:
            decimal_part = self.frac(numerator-int_part*denominator, denominator)
            ret = str(int_part)+"."+decimal_part
        ____
            ret = str(int_part)

        __ sign < 0:
            ret = "-" + ret

        r_ ret

    ___ frac(self, num, deno
        """
        real fraction part
        """
        ret = []
        d = {}
        i = 0

        w___ num:
            num *= 10
            q = num/deno
            r = num%deno
            __ (q, r) in d:
                ret.append(")")
                ret.insert(d[(q, r)], "(")
                r_ "".join(ret)

            ret.append(str(q))
            d[(q, r)] = i
            i += 1
            num -= q*deno

        r_ "".join(ret)


class Solution_error:
    ___ fractionToDecimal(self, numerator, denominator
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
        ____
            ret = str(int_part)

        r_ ret

    ___ frac(self, num, deno
        """
        real fraction part
        """
        ret = []
        d = {}
        i = 0

        w___ num:
            l = 0  # the number of added 0
            w___ num < deno:
                num *= 10
                l += 1

            r = num/deno
            __ r in d:
                ret.append(")")
                ret.insert(d[r]-(l-1), "(")
                r_ "".join(ret)

            ___ _ in xrange(l-1
                ret.append("0")
                i += 1

            ret.append(str(r))
            d[r] = i
            i += 1
            num -= r*deno

        r_ "".join(ret)

__ __name__ __ "__main__":
    assert Solution().fractionToDecimal(1, 333) __ "0.(003)"
    assert Solution().fractionToDecimal(1, 90) __ "0.0(1)"
    assert Solution().fractionToDecimal(-50, 8) __ "-6.25"
    assert Solution().fractionToDecimal(7, -12) __ "-0.58(3)"