#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ letterCombinations  digits
        """
        :type digits: str
        :rtype: List[str]
        """

        phone_letters = {0: [" "],
                         1: ["*"],
                         2: ["a", "b", "c"],
                         3: ["d", "e", "f"],
                         4: ["g", "h", "i"],
                         5: ["j", "k", "l"],
                         6: ["m", "n", "o"],
                         7: ["p", "q", "r", "s"],
                         8: ["t", "u", "v"],
                         9: ["w", "x", "y", "z"],
                         }
        __ digits:
            all_str = phone_letters[ord(digits[0]) - ord("0")]
        ____
            r_ []

        ___ i __ r..(1, l..(digits)):
            all_str = self.combination(
                all_str,
                phone_letters[ord(digits[i]) - ord("0")])

        r_ all_str

    # return string which combines a in str_a with b in str_b
    ___ combination  str_a, str_b
        combine_str   # list
        ___ a __ str_a:
            ___ b __ str_b:
                combine_str.append(a + b)

        r_ combine_str

"""
""
"37"
"1234"
"""
