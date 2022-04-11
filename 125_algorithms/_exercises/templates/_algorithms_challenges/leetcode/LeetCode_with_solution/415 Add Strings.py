#!/usr/bin/python3
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


c_ Solution:
    ___ i..  n
        r.. o..(n) - o..("0")

    ___ addStrings  num1, num2
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret    # list
        # let num2 to be one has more digit
        __ l..(num1) > l..(num2
            num1, num2 num2, num1

        num1 num1[::-1]
        num2 num2[::-1]
        carry 0
        idx 0
        w.... idx < l..(num2
            __ idx < l..(num1
                s i..(num1[idx]) + i..(num2[idx]) + carry
            ____
                s i..(num2[idx]) + carry

            __ s >_ 10:
                s -_ 10
                carry 1
            ____
                carry 0

            ret.a..(s)
            idx += 1

        __ carry:
            ret.a..(carry)

        r.. "".j.. m..(s.., ret[::-1]


__ _______ __ _______
    ... Solution().addStrings("9999", "1") __ "10000"
    ... Solution().addStrings("9999", "9999") __ "19998"
    ... Solution().addStrings("23", "8") __ "31"
