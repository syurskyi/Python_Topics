_______ p__

____ thumbs _______ Thumbs


@p__.f..(scope="module")
___ thumbs
    r.. Thumbs()


@p__.mark.parametrize("arg, expected", [
    (-10, "👎 (10x)"),
    (-9, "👎 (9x)"),
    (-8, "👎 (8x)"),
    (-7, "👎 (7x)"),
    (-6, "👎 (6x)"),
    (-5, "👎 (5x)"),
    (-4, "👎 (4x)"),
    (-3, "👎👎👎"),
    (-2, "👎👎"),
    (-1, "👎"),
    (1, "👍"),
    (2, "👍👍"),
    (3, "👍👍👍"),
    (4, "👍 (4x)"),
    (5, "👍 (5x)"),
    (6, "👍 (6x)"),
    (7, "👍 (7x)"),
    (8, "👍 (8x)"),
    (9, "👍 (9x)"),
    (10, "👍 (10x)"),
])
___ test_operator_overloading_works_both_ways(arg, expected, thumbs):
    ... thumbs * arg __ arg * thumbs __ expected


___ test_exception(thumbs):
    w__ p__.r..(ValueError):
        thumbs * 0
    w__ p__.r..(ValueError):
        0 * thumbs
