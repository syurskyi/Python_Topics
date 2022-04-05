"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ = 'Danyang'
int2roman = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",

    10: "X",
    40: "XL",
    50: "L",
    90: "XC",

    100: "C",
    400: "CD",
    500: "D",
    900: "CM",

    1000: "M"
}


c_ Solution:
    ___ intToRoman  num
        """
        dealing with digits
        notice the 1, 4, 5, 9, 10 repetition

        :param num: integer, Input is guaranteed to be within the range from 1 to 3999
        :return: a string
        """
        string_builder    # list
        components = [1, 4, 5, 9, 10, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        # starting from the largest
        ___ component __ r..(components  # reversed
            w.... num >_ component:
                string_builder.a..(int2roman[component])
                num -_ component

        r.. "".j..(string_builder)