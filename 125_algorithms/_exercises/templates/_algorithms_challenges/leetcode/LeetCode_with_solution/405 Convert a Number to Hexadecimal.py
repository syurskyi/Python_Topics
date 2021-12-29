"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two's complement method is
used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""
__author__ = 'Daniel'


class Solution(object):
    ___ toHex(self, num):
        """
        All use bit manipulation
        :type num: int
        :rtype: str
        """
        ret    # list
        w.... l..(ret) < 8 a.. num:
            ret.a..(self.encode(num & 0xf))
            num >>= 4

        r.. ''.join(ret[::-1]) o. '0'

    ___ toHexNormal(self, num):
        """
        Python arithmetic handles the negative number very well
        :type num: int
        :rtype: str
        """
        ret    # list
        w.... l..(ret) < 8 a.. num:
            ret.a..(self.encode(num % 16))
            num /= 16

        r.. ''.join(ret[::-1]) o. '0'

    ___ encode(self, d):
        __ 0 <= d < 10:
            r.. s..(d)

        r.. chr(ord('a') + d - 10)


__ __name__ __ "__main__":
    ... Solution().toHex(-1) __ 'ffffffff'
