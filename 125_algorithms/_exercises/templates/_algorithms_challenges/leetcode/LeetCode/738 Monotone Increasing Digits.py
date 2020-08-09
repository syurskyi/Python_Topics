#!/usr/bin/python3
"""
Given a non-negative integer N, find the largest number that is less than or
equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair
of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""


class Solution:
    ___ monotoneIncreasingDigits(self, N: int) -> int:
        """
        332
        322
        222
        fill 9
        299
        """
        digits = [int(e) ___ e in str(N)]
        pointer = le.(digits)
        ___ i in range(le.(digits) - 1, 0, -1
            __ digits[i - 1] > digits[i]:
                pointer = i
                digits[i - 1] -= 1

        ___ i in range(pointer, le.(digits)):
            digits[i] = 9

        r_ int("".join(map(str, digits)))


__ __name__ __ "__main__":
    assert Solution().monotoneIncreasingDigits(10) __ 9
    assert Solution().monotoneIncreasingDigits(332) __ 299
