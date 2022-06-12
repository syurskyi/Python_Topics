# _______ p__
#
# ____ ? _______ ?
#
# TEXTS =  'Hello world', 'Welcome to PyBites',
#          'Decorators for fun and profit'
#
#
# ?p__.m__.p. "start, end, arg, expected", [
#     (3, 5, ?[0], 'Hel.. world'),
#     (4, 8, ?[0], 'Hell....rld'),
#     (0, 3, ?[1], '...come to PyBites'),
#     (-1, 3, ?[1], '...come to PyBites'),
#     (0, -1, ?[1], 'Welcome to PyBites'),
#     (5, 10, ?[2], 'Decor..... for fun and profit'),
#     (100, 110, ?[2], 'Decorators for fun and profit'),
#     (20, 100, ?[2], 'Decorators for fun a.........'),
#
# ___ test_strip_range start end arg e..
#     ?? ? ?
#     ___ gen_output text
#         r.. ?
#     a.. ? ?_a..
#     ... a.. __ e..