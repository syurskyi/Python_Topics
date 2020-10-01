# Integer to Roman
# Question: Given an integer, convert it to a roman numeral
# Input is guaranteed to be within the range from 1 to 3999.
# Solutions:


c_ Solution:
    # @return a string

    ___ intToRoman(self, num):
        v.. _ [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals _ [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        li.. _ ''
        ___ i __ ra..(0, le.(v..)):
            w___ num >_ v..[i]:
                num -_ v..[i]
                li.. +_ numerals[i]
        r_ li..


Solution().intToRoman(1001)