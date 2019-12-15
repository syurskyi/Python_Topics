# from typing import List
#
# c_ User
#     ___ - ____ first_name s.. last_name s..
#         ____.f.. _ f..
#         ____.l. _ l..
#
#     ___ get_full_name ____
#         r_ ____.f.. + ' ' + ____.l..
#
#
# ___ create_users_v1 first_names l.. last_names l..  l..
#     users _    # list
#     items _ z.. f_s l_s
#     ___ f.. l... i_ ?
#         # first_name.?????
#         u__.ap.. U.. f... l...
#     r_ u..
#
#
# ___ create_users_v2 first_names L.. s..,
#                     last_names L.. s.. __ L.. U..
#     users _      # list
#     items _ zi. f...s l...s
#     ___ f... l... i_ ?
#         # first_name.AUTOCOMPLETE
#         u___.ap.. U.. f... l...
#     r_ u..
#
#
# users1 = create_users_v2(['f1', 'f2'], ['l1', 'l2'])
# users2 = create_users_v2(['f1', '10'], ['10.5', 'l2'])
# users3 = create_users_v2(['f1', 'f2'], ['[]', 'l2'])
# print(users2[0].get_full_name())
