"""
7 kyu: Money, Money, Money
http://www.codewars.com/kata/563f037412e5ada593000114/train/python
"""


___ calculate_years(principal, interest, tax, desired
    __ principal >= desired:
        r_ 0
    result = principal * interest * (1 - tax) + principal
    r_ 1 __ result >= desired else 1 + calculate_years(result, interest, tax, desired)
