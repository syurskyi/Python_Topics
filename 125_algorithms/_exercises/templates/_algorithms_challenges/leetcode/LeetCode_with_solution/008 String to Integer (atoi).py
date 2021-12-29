"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather
all the input requirements up front.
"""
__author__ = 'Danyang'


class Solution:
    ___ atoi(self, str):
        """
        Need to satisfy all the nuance requirements

        :param str: string
        :return: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # clean
        str = str.strip()
        __ n.. str:
            r.. 0

        # clean up leading sign
        sign = 1
        __ str[0] __ ("+", "-"):
            __ str[0] __ "-":
                sign = -1
            str = str[1:]

        # check for leading digit
        __ n.. str[0].isdigit():
            r.. 0

        # ignore the non-digit appended behind
        # The string can contain additional characters after those that form the integral number,
        # which are ignored and have no effect on the behavior of this function
        ___ ind, val __ enumerate(str):  # find the 1st non-digit
            __ n.. val.isdigit():
                str = str[:ind]
                break




        # convert char array to integer
        s.. = 0
        scale = 1
        ___ element __ str[::-1]:
            s.. += scale*int(element)
            scale *= 10

        # return sign*sum, and pay attention to the C constraints
        result = sign*s..
        __ result > INT_MAX:
            r.. INT_MAX
        __ result < INT_MIN:
            r.. INT_MIN
        r.. result
