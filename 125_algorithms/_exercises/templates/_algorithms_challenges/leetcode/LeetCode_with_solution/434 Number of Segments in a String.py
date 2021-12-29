#!/usr/bin/python3
"""
Count the number of segments in a string, where a segment is defined to be a
contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.
"""


class Solution:
    ___ countSegments(self, s):
        """
        I could use split but it may not be the intention of this problem

        :type s: str
        :rtype: int
        """
        ret = 0
        __ not s:
            return ret

        # count at start
        __ s[0] != " ":
            ret = 1
        prev = s[0]
        for c in s[1:]:
            __ c != " " and prev == " ":
                ret += 1
            prev = c
        return ret


__ __name__ == "__main__":
    assert Solution().countSegments("Hello, my name is John") == 5
