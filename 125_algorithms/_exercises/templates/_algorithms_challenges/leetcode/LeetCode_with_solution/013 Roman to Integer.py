"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ 'Danyang'
roman2int {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


c_ Solution:
    ___ romanToInt  s
        """
        What happens if current roman char larger than the previous roman char?

        :param s: String
        :return: integer
        """
        result 0
        ___ ind, val __ e..(s
            __ ind > 0 a.. roman2int[val] > roman2int[s[ind-1]]:  # e.g. XIV
                result -_ roman2int[s[ind-1]]  # reverse last action
                result += roman2int[val]-roman2int[s[ind-1]]
            ____
                result += roman2int[val]

        r.. ?




