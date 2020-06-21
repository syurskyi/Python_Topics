# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# *TL;DR80
# Encapsulates all information needed to perform an action or trigger an event.
# """
#
# ____ -f ______ p..
# ______ __
# ____ __.pa.. ______ lex..
#
#
# c__ MoveFileCommand o..
#
#     ___ - src dest
#         ? ?
#         ? ?
#
#     ___ execute
#         re.. s.. d..
#
#     ___ undo
#         re.. d.. s..
#
#     ___ rename  src dest
#         print(u"renaming @ to @"  ? ?
#         __.re.. ? ?
#
#
# ___ main
#     command_stack _    # list
#
#     # commands are just pushed into the command stack
#     ?.ap.. M... 'foo.txt', 'bar.txt'
#     ?.ap.. M.. 'bar.txt', 'baz.txt'
#
#     # verify that none of the target files exist
#     ass.. no. le.. "foo.txt
#     ass.. no. le.. "bar.txt
#     ass.. no. le.. "baz.txt
#     ___
#         w___ o.. foo.txt _  # Creating the file
#             p..
#
#         # they can be executed later on
#         ___ cmd __ c_s..
#             ?.e..
#
#         # and can also be undone at will
#         ___ cmd __ re.. c_s..
#             ?.u..
#     f....
#         __.u.. foo.txt
#
# __ _______ __ ______
#     ?
#
# ### OUTPUT ###
# # renaming foo.txt to bar.txt
# # renaming bar.txt to baz.txt
# # renaming baz.txt to bar.txt
# # renaming bar.txt to foo.txt
