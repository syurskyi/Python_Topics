_______ p__

____ Previous.decorator _______ strip_range

TEXTS = ['Hello world', 'Welcome to PyBites',
         'Decorators for fun and profit']


@p__.mark.parametrize("start, end, arg, expected", [
    (3, 5, TEXTS[0], 'Hel.. world'),
    (4, 8, TEXTS[0], 'Hell....rld'),
    (0, 3, TEXTS[1], '...come to PyBites'),
    (-1, 3, TEXTS[1], '...come to PyBites'),
    (0, -1, TEXTS[1], 'Welcome to PyBites'),
    (5, 10, TEXTS[2], 'Decor..... for fun and profit'),
    (100, 110, TEXTS[2], 'Decorators for fun and profit'),
    (20, 100, TEXTS[2], 'Decorators for fun a.........'),
])
___ test_strip_range(start, end, arg, expected):
    @strip_range(start, end)
    ___ gen_output(text):
        r.. text
    actual = gen_output(text=arg)
    ... actual __ expected