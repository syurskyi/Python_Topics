# #!/usr/bin/env python3
# """Change permissions on a file
# """
#
# #end_pymotw_header
# ______ __
# ______ s..
#
# filename _ 'os_stat_chmod_example.txt'
# __ __.p...e.. ?
#     __.u.. ?
# w__ o.. ? __ __ f
#     ?.w.. 'contents'
#
# # Determine what permissions are already set using stat
# existing_permissions _ s...S_IM.. __.s.. ? .s_m..
#
# __ no. __.a.. ? __.X_
#     print('Adding execute permission')
#     new_permissions _ ? _ s...S_IX..
# ____
#     print('Removing execute permission')
#     # use xor to remove the user execute permission
#     new_permissions _ ? _ s...S_IX..
#
# __.c_m.. f.. ?
