____ collections _______ OrderedDict
____ functools _______ reduce

# NUMERALS = OrderedDict(((1000, 'M'), (500, 'D'), (100, 'C'),
#                         (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')))

NUMERALS = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
NUMS = l..(r..(l..(NUMERALS.keys())))


___ romanutil(n: i.., queue: l..):
    '''utility function for romanize recursive implementation'''
    print(f'entering romanutil with {n=}')
    print(f'{NUMS=}')
    chars = ''
    remainder = 0
    __ n __ NUMERALS:
        chars = NUMERALS[n]
        queue.a..(chars)
        remainder = 0
        r..

    ___ k __ NUMS:
        __ k < n:
            quotient = n // k
            remainder = n % k
            chars = chars + NUMERALS[k] * quotient
            print(f'{chars=}')
            queue.a..(chars)
            break

    __ remainder __ 0:
        r..
    ____:
        romanutil(remainder, queue)


___ romanize(decimal_number: i..):
    """Takes a decimal number int and converts its Roman Numeral str"""

    __ n.. isi..(decimal_number, i..) o. 4000 <= decimal_number <= 0:
        r.. ValueError

    roman    # list
    romanutil(decimal_number, roman)
    roman_string = ''.j..(roman)
    r.. roman_string
