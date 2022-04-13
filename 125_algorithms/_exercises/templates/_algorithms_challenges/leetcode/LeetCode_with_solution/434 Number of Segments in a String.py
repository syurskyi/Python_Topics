#!/usr/bin/python3
"""
Count the number of segments in a string, where a segment is defined to be a
contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.
"""


c_ Solution:
    ___ countSegments  s
        """
        I could use split but it may not be the intention of this problem

        :type s: str
        :rtype: int
        """
        ret 0
        __ n.. s:
            r.. ret

        # count at start
        __ s[0] !_ " ":
            ret 1
        prev s[0]
        ___ c __ s 1|
            __ c !_ " " a.. prev __ " ":
                ret += 1
            prev c
        r.. ret


__ _______ __ _______
    ... Solution().countSegments("Hello, my name is John") __ 5
