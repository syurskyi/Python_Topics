from collections import OrderedDict
from functools import reduce

# NUMERALS = OrderedDict(((1000, 'M'), (500, 'D'), (100, 'C'),
#                         (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')))

NUMERALS = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
NUMS = list(reversed(list(NUMERALS.keys())))


___ romanutil(n: int, queue: list):
    '''utility function for romanize recursive implementation'''
    print(f'entering romanutil with {n=}')
    print(f'{NUMS=}')
    chars = ''
    remainder = 0
    __ n in NUMERALS:
        chars = NUMERALS[n]
        queue.append(chars)
        remainder = 0
        return

    for k in NUMS:
        __ k < n:
            quotient = n // k
            remainder = n % k
            chars = chars + NUMERALS[k] * quotient
            print(f'{chars=}')
            queue.append(chars)
            break

    __ remainder == 0:
        return
    else:
        romanutil(remainder, queue)


___ romanize(decimal_number: int):
    """Takes a decimal number int and converts its Roman Numeral str"""

    __ not isinstance(decimal_number, int) or 4000 <= decimal_number <= 0:
        raise ValueError

    roman = []
    romanutil(decimal_number, roman)
    roman_string = ''.join(roman)
    return roman_string
