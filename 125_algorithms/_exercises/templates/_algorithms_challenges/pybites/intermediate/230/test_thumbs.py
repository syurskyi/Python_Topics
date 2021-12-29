import pytest

from thumbs import Thumbs


@pytest.fixture(scope="module")
___ thumbs():
    return Thumbs()


@pytest.mark.parametrize("arg, expected", [
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
    assert thumbs * arg == arg * thumbs == expected


___ test_exception(thumbs):
    with pytest.raises(ValueError):
        thumbs * 0
    with pytest.raises(ValueError):
        0 * thumbs