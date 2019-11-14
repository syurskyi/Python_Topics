# l_ z_ r_ 5 r_ 100
# # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
#
# # If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip().
# # With this function, the missing values will be replaced with whatever you pass to the fillvalue argument
# # (defaults to None). The iteration will continue until the longest iterable is exhausted:
#
# f.. it.... _____ z.._l..
# numbers _ 1 2 3
# letters _ 'a' 'b' 'c'
# longest _ r_ 5
# zipped _ z.._l.... n... l.... l...., f...v..._ ?
# l_ z....
# # [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]