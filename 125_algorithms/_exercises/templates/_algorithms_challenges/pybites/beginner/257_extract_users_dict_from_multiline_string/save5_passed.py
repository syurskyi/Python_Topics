# _______ __
#
# ___ get_users passwd
# s..  __ d..
#     """Split password output by newline,
#       extract user and name (1st and 5th columns),
#       strip trailing commas from name,
#       replace multiple commas in name with a single space
#       return dict of keys = user, values = name.
#     """
#     passwd  p__.s...s..
#     keys    # list
#     values    # list
#     ___ p __ p..
#         k__.a.. p.s.. ':' 0
#         __ l.. p.s.. ':' 4  __ 0
#             ?.a.. 'unknown'
#         ____
#             ?.a.. ' '.j..
#                 __.s.. ',' ' ' ?.s.. ':' 4 .s..
#     r.. d.. z.. ? ?