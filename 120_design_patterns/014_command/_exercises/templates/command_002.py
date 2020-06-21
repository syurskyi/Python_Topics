# # -*- coding: utf8 -*-
#
# ____ ___ ______ stdout as console
#
#
# # Handling 'exit' command
# c_ SessionClosed E..
#     ___ - value
#         ?  ?
#
#
# # Interface
# c_ Command
#     ___ execute
#         r_ N...
#
#     ___ cancel
#         r_ N...
#
#     ___ name
#         r_ N...
#
#
# # rm command
# c_ RmCommand C..
#     ___ execute
#         c___.w.. ("You are executed \"rm\" command\n")
#
#     ___ cancel
#         c___.w.. ("You are canceled \"rm\" command\n")
#
#     ___ name
#         r_ "rm"
#
#
# # uptime command
# c_ UptimeCommand C..
#     ___ execute
#         c___.w.. ("You are executed \"uptime\" command\n")
#
#     ___ cancel
#         c___.w.. ("You are canceled \"uptime\" command\n")
#
#     ___ name
#         r_ "uptime"
#
#
# # undo command
# c_ UndoCommand C..
#     ___ execute
#         ___
#             cmd _ H___.p..
#             T___.ap.. ?
#             c___.w.. ("Undo command \"@\"\n".f.. ?.n..
#             ?.c..
#
#         ______ I...
#             c___.w.. ("ERROR: HISTORY is empty\n")
#
#     ___ name
#         r_ "undo"
#
#
# # redo command
# c_ RedoCommand C..
#     ___ execute
#         ___
#             cmd _ T___.p..
#             H___.ap.. ?
#             c___.w.. ("Redo command \"{0}\"\n".f.. ?.n..
#             ?.ex..
#         ______ I..
#             c___.w.. ("ERROR: TRASH is empty\n")
#
#     ___ name
#         r_ "redo"
#
#
# # history command
# c_ HistoryCommand C..
#     ___ execute
#         i _ 0
#         ___ cmd in H..
#             c___.w.. ("@: @\n".f.. i ?.n..
#             i _ i + 1
#
#     ___ name
#         print "history"
#
#
# # exit command
# c_ ExitCommand C..
#     ___ execute
#         r_ S.. "Good day!"
#
#     ___ name
#         r_ "exit"
#
# # available commands
# COMMANDS _ {*rm R.. *uptime U.. *undo
#             U.. *redo R.. *history H..
#             *exit E..
#
# HISTORY _ l..
# TRASH _ l..
#
#
# # Shell
# ___ main
#     ___
#         w___ T..
#             c___.fl..
#             c___.w.. ("pysh >> ")
#
#             cmd _ r_i..
#
#             ___
#                 command _ C..|?
#                 ?.ex..
#                 __ |no. isi.. c..., U.. an. no.
#                     isi.. c..., R... an. no.
#                     isi.. c..., H..
#                     T.._ l..
#                     H___.ap.. c..
#
#             ______ KeyError
#                 c___.w.. ("ERROR: Command \"@\" not found\n"  ?
#
#     ______ SessionClosed __ e
#         c___.w..  ?.v..
#
# __ _______ __ ______
#     ?
