#!/usr/bin/python3
"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""


c_ Solution:
    ___ convertToBase7  num
        """
        simplfied for negative number
        :type num: int
        :rtype: str
        """
        __ num __ 0:
            r.. "0"
        ret    # list
        n = abs(num)
        w.... n:
            ret.a..(n % 7)
            n //= 7

        ret = "".j.. m..(s.., ret[::-1]))
        __ num < 0:
            ret = "-" + ret

        r.. ret


__ _______ __ _______
    ... Solution().convertToBase7(100) __ "202"
    ... Solution().convertToBase7(-7) __ "-10"
