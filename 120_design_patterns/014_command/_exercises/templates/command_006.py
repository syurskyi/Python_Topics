# """
# *TL;DR
# Encapsulates all information needed to perform an action or trigger an event.
#
# *Examples in Python ecosystem:
# Django HttpRequest (without `execute` method):
#  https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
# """
#
# _____ __
#
#
# c_ MoveFileCommand
#     ___ - src dest
#         ?  ?
#         ?  ?
#
#     ___ execute
#         re.. s.. d..
#
#     ___ undo
#         re.. d.. s..
#
#     ___ rename src dest
#         print("renaming @ to @".f.. ? ?
#         __.re.. ? ?
#
#
# ___ main
#
#     ____ __.pa.. _____ lex..
#
#     command_stack _ |
#         M.. 'foo.txt', 'bar.txt'
#         M.. 'bar.txt', 'baz.txt'
#     |
#
#     # Verify that none of the target files exist
#     ass.. no. lex... "foo.txt"
#     ass.. no. lex... "bar.txt"
#     ass.. no. lex... "baz.txt"
#
#     # Create empty file
#     o.. foo.txt _ .cl..
#
#     # Commands can be executed later on
#     ___ cmd __ c_s..
#         ?.ex..
#     # renaming foo.txt to bar.txt
#     # renaming bar.txt to baz.txt
#
#     # And can also be undone at will
#     ___ cmd __ re.. c_s..
#         ?.u..
#     # renaming baz.txt to bar.txt
#     # renaming bar.txt to foo.txt
#
#     __.un.. foo.txt
#
#
#
# __ _______ __ ______
#     ?
