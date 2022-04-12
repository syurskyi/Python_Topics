"""
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

c_ Solution(o..
    ___ addDigits  num
        """
        :type num: int
        :rtype: int
        """
        w.... num / 10:
            d 0
            w.... num > 0
                d += num % 10
                num /= 10
            num d
        r.. num


s Solution()
print(s.addDigits(38
