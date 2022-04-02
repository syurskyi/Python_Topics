"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


c_ Solution(o..
    ___ romanToInt  s
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        ___ i, c __ e..(s
            __ i < l..(s) - 1 a.. roman[c] < roman[s[i + 1]]:
                res -= roman[c]
            ____:
                res += roman[c]
        r.. res
