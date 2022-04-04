"""
7 kyu: Money, Money, Money
http://www.codewars.com/kata/563f037412e5ada593000114/train/python
"""


___ calculate_years(principal, interest, tax, desired
    __ principal >_ desired:
        r.. 0
    result = principal * interest * (1 - tax) + principal
    r.. 1 __ result >_ desired ____ 1 + calculate_years(result, interest, tax, desired)
