"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
__author__ = 'Danyang'


class Solution(object):
    ___ reverse(self, x):
        """
        Sign for preserving negative number of positive number
        :param x: int
        :return: int
        """
        sign = -1 __ x < 0 ____ 1  # preserve the sign first
        x *= sign

        # eliminated leading zero in the reversed integer
        w.... x:
            __ x%10 __ 0:
                x /= 10
            ____:
                break

        # string manipulation
        x = s..(x)
        lst = l..(x)  # list('123') returns ['1', '2', '3']
        lst.reverse()
        x = "".join(lst)
        x = int(x)
        r.. sign*x


__ __name__ __ "__main__":
    print Solution().reverse(123)

