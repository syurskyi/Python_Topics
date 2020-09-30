# Integer to Roman
# Question: Given an integer, convert it to a roman numeral
# Input is guaranteed to be within the range from 1 to 3999.
# Solutions:


class Solution:
    # @return a string

    ___ intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        ___ i __ range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        r_ list


Solution().intToRoman(1001)