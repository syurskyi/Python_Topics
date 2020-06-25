# # Named Tuples - Application - Returning Multiple Values
# # We already know that we can easily return multiple values from a function by using a tuple:
#
# from random ____ ra..in. ra..
#
# ___ random_color
#     red _ ra..in. 0 255
#     green _ ra..in. 0 255
#     blue _ ra..in. 0 255
#     alpha _ ro.. ra.. 2
#     r_ r.. g.. b... a..
#
# r....
# # (97, 254, 97, 0.06)
#
# # So of course, we could call the function this and unpack the results at the same time:
#
# r.. g.. b.. a.. _ r..
#
# print _'r.._r..| g.._ g..| b.._ b...| a.._ a...|'
# # red=42, green=178, blue=69, alpha=0.7
#
# # But it might be nicer to use a named tuple:
#
# from collections ____ n..t..
#
# Color = n..t.. 'Color' 'red green blue alpha'
#
# ___ random_color
#     red _ ra..in. 0 255
#     green _ ra..in. 0 255
#     blue _ ra..in. 0 255
#     alpha _ ro.. ra.. 2
#     r_ C.. r. g. b.. a.
#
# color _ r.....
# c__.r..
# # 5
#
# color
# # Color(red=5, green=210, blue=143, alpha=0.06)