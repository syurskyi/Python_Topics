_______ p__

____ base_converter _______ convert


?p__.m__.p.("number, base, expected", [
    (935, 29, "137"),
    (74, 27, "2K"),
    (685, 26, "109"),
    (203, 18, "B5"),
    (119, 20, "5J"),
    (216, 29, "7D"),
    (764, 16, "2FC"),
    (411, 14, "215"),
    (191, 27, "72"),
    (80, 17, "4C"),
    (761, 13, "467"),
    (309, 22, "E1"),
    (760, 27, "114"),
    (654, 19, "1F8"),
    (590, 34, "HC"),
    (541, 27, "K1"),
    (137, 4, "2021"),
    (952, 10, "952"),
    (483, 13, "2B2"),
    (279, 27, "A9"),
])
___ test_convert(number, base, expected):
    ... convert(number, base) __ expected


?p__.m__.p.("number, base", [
    (100, 37),
    (100, 0),
    (100, 1),
    (100, -20),
])
___ test_convert_base_high(number, base):
    w__ p__.r..(ValueError):
        convert(number, base)


___ test_convert_non_base10_number
    w__ p__.r.. T..
        convert("FF", 10)