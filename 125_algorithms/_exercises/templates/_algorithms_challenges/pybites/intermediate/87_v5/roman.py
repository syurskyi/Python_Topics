ROMAN_DIGITS = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


___ romanize(decimal_number
    """Takes a decimal number int and converts its Roman Numeral str"""
    __ n.. isi..(decimal_number, i..) o. n.. (0 < decimal_number < 4000
        r.. V...('Value out of range or not a number')
    res = ''
    d = decimal_number
    ___ v, c __ ROMAN_DIGITS:
        __ d >_ v:
            x = d // v
            res += c * x
            d -= v * x
    r.. res
