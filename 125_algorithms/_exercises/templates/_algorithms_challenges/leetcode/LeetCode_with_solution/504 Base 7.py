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


class Solution:
    ___ convertToBase7(self, num):
        """
        simplfied for negative number
        :type num: int
        :rtype: str
        """
        __ num == 0:
            return "0"
        ret = []
        n = abs(num)
        while n:
            ret.append(n % 7)
            n //= 7

        ret = "".join(map(str, ret[::-1]))
        __ num < 0:
            ret = "-" + ret

        return ret


__ __name__ == "__main__":
    assert Solution().convertToBase7(100) == "202"
    assert Solution().convertToBase7(-7) == "-10"
