_______ p__

____ ? _______ ?


?p__.m__.p.("color, expected", [
    ("white", (255, 255, 255,
    ("black", (0, 0, 0,
    ("blue", (0, 0, 255,
    ("red", (255, 0, 0,
    ("green", (0, 128, 0,
    ("orange", (255, 128, 0,
    ("puke", N..),
])
___ test_color_class color e..
    c ? ?
    ... ?.r.. __ e..


?p__.m__.p.("rgb, expected", [
    ((255, 255, 255), "#ffffff"),
    ((0, 0, 0), "#000000"),
    ((0, 0, 255), "#0000ff"),
    ((255, 0, 0), "#ff0000"),
    ((0, 128, 0), "#008000"),
    ((255, 128, 0), "#ff8000"),
])
___ test_color_staticmethod_rgb2hex rgb, e..
    ... ?.r.. ?) __ e..


?p__.m__.p.("rgb", [
    ("puke"),
    ("0, 0, 0"),
    ((0, -5, 255,
    ((256, 0, 0,
])

___ test_color_rgb2hex_bad_value rgb
    w__ p__.r..(V...
        ?.r.. ?)


?p__.m__.p.("hex, expected", [
    ("#ffffff", (255, 255, 255,
    ("#000000", (0, 0, 0,
    ("#0000ff", (0, 0, 255,
    ("#ff0000", (255, 0, 0,
    ("#008000", (0, 128, 0,
    ("#ff8000", (255, 128, 0,
])
___ test_color_staticmethod_hex2rgb(hex, e..
    ... ?.h.. ? __ e..

?p__.m__.p.("value", [
    ("puke"),
    ("#ccc"),
    ("#stopit"),
    ("pink"),
])
___ test_color_hex2rgb_bad_value(value
    w__ p__.r..(V...
        ?.h.. ?


___ test_color_string_output
    color Color("brown")
    ... s..(color) __ "(165, 42, 42)"

___ test_color_repr_output
    color Color("brown")
    ... r.. (color) __ "Color('brown')"


___ test_unknown_color
    color Color("puke green")
    ... s..(color) __ "Unknown"
