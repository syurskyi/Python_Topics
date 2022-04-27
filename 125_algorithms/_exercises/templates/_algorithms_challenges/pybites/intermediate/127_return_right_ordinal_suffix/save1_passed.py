# ___ get_ordinal_suffix number
#     '''Receives an int and returns it appended with its ordinal suffix,
#        so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.'''
#     __ 11 <_ ? % 100 <_ 13
#         ordinal 'th'
#     ____ s.. ? -1 __ '1'
#         ? 'st'
#     ____ s.. ? -1 __ '2'
#         ? 'nd'
#     ____ s.. ? -1 __ '3'
#         ? 'rd'
#     ____
#         ? 'th'
#     r.. s.. ? + ?