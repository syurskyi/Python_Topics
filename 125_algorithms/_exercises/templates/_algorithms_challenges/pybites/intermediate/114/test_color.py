_______ p__

____ color _______ Color


@p__.mark.parametrize("color, expected", [
    ("white", (255, 255, 255)),
    ("black", (0, 0, 0)),
    ("blue", (0, 0, 255)),
    ("red", (255, 0, 0)),
    ("green", (0, 128, 0)),
    ("orange", (255, 128, 0)),
    ("puke", N..),
])
___ test_color_class(color, expected):
    c = Color(color)
    ... c.rgb __ expected


@p__.mark.parametrize("rgb, expected", [
    ((255, 255, 255), "#ffffff"),
    ((0, 0, 0), "#000000"),
    ((0, 0, 255), "#0000ff"),
    ((255, 0, 0), "#ff0000"),
    ((0, 128, 0), "#008000"),
    ((255, 128, 0), "#ff8000"),
])
___ test_color_staticmethod_rgb2hex(rgb, expected):
    ... Color.rgb2hex(rgb) __ expected


@p__.mark.parametrize("rgb", [
    ("puke"),
    ("0, 0, 0"),
    ((0, -5, 255)),
    ((256, 0, 0)),
])

___ test_color_rgb2hex_bad_value(rgb):
    w__ p__.r..(ValueError):
        Color.rgb2hex(rgb)


@p__.mark.parametrize("hex, expected", [
    ("#ffffff", (255, 255, 255)),
    ("#000000", (0, 0, 0)),
    ("#0000ff", (0, 0, 255)),
    ("#ff0000", (255, 0, 0)),
    ("#008000", (0, 128, 0)),
    ("#ff8000", (255, 128, 0)),
])
___ test_color_staticmethod_hex2rgb(hex, expected):
    ... Color.hex2rgb(hex) __ expected


@p__.mark.parametrize("value", [
    ("puke"),
    ("#ccc"),
    ("#stopit"),
    ("pink"),
])
___ test_color_hex2rgb_bad_value(value):
    w__ p__.r..(ValueError):
        Color.hex2rgb(value)


___ test_color_string_output
    color = Color("brown")
    ... s..(color) __ "(165, 42, 42)"


___ test_color_repr_output
    color = Color("brown")
    ... repr(color) __ "Color('brown')"


___ test_unknown_color
    color = Color("puke green")
    ... s..(color) __ "Unknown"
