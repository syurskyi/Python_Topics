#!/usr/bin/python3
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    ___ int(self, n):
        return ord(n) - ord("0")

    ___ addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        # let num2 to be one has more digit
        __ len(num1) > len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        idx = 0
        while idx < len(num2):
            __ idx < len(num1):
                s = self.int(num1[idx]) + self.int(num2[idx]) + carry
            else:
                s = self.int(num2[idx]) + carry

            __ s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0

            ret.append(s)
            idx += 1

        __ carry:
            ret.append(carry)

        return "".join(map(str, ret[::-1]))


__ __name__ == "__main__":
    assert Solution().addStrings("9999", "1") == "10000"
    assert Solution().addStrings("9999", "9999") == "19998"
    assert Solution().addStrings("23", "8") == "31"
