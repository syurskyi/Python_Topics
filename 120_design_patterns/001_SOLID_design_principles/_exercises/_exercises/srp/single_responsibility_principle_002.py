# #  Single-Responsibility Principle (SRP)
#
# # Gather together the things that change for the same reasons. Separate those things that change for different reasons
#
#
# ____ d..t.. ______ d..t..
#
#
# c_ Journal
#     # Journal formats entries
#     ___ -
#         ?entries    # list
#         ?count _ 1
#
#     ___ add_entry  text ? timestamp d_t_  d_t__.to... __ N..
#         ?e___.ap.. _*|?c.. . |t.. "
#         ?c... +_ 1
#
#     ___ -s
#         r_ "\n".jo.. ?e..
#
#     # Journal saves itself
#     ___ save filename ? __ N..
#         w.. o.. ? _ __ f
#             ?.w.. st. ____
#
#
# c_ StorageManager
#     # StorageManager saves things into long-term memory
#     ___ save_journal journal J.. filename ? __ N..
#         w.. o.. ? _ __ f
#             ?.w.. st. j..
#
#
# __ ______ __ ______
#     journal = J..
#     ?.a_e..("Today, I'm learning the Single-Responsibility Principle.")
#     ?.a_e..("Tomorrow, I'll learn about the Open-Close Principle.")
#     print ?
