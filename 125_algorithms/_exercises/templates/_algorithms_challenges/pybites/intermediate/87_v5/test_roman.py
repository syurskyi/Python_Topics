_______ p__

____ roman _______ romanize


@p__.m__.p..("number, numeral", [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
    (177, 'CLXXVII'),
    (244, 'CCXLIV'),
    (87, 'LXXXVII'),  # Bite LXXXVII
    (1033, 'MXXXIII'),
    (997, 'CMXCVII'),
    (3999, 'MMMCMXCIX'),
    (13, 'XIII'),
    (777, 'DCCLXXVII'),
    (1652, 'MDCLII'),
    (1981, 'MCMLXXXI'),
    (2018, 'MMXVIII'),
    (3500, 'MMMD'),
])
___ test_romanize(number, numeral):
    ... romanize(number) __ numeral


___ test_boundaries
    w__ p__.r..(ValueError):
        romanize('string')
        romanize(-1)
        romanize(0)
        romanize(4000)
        romanize(10000)