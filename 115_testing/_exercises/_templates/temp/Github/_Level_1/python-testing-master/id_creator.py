# c_ IdCreator
#
#     ___ faculty_id  value
#         __ no. isi.. ? __.
#             r_ T..('Only integer values allowed')
#         __ ? < 0
#             r_ V..('Only positive values allowed')
#         __ ? __ 0
#             r_ 1
#         ____:
#             r_ ?(?-1) * ?
#
#
# # Testing without using a framework
# __ _____ __ _____
#     creator _ ?
#     a.. ?.f.. 0 __ 1
#     a.. ?.f.. 3 __ 6
#
#     ___
#         ?.f.. -1
#         a.. 1 __ 0
#     _____ V..
#         p..
#
#     ___
#         ?.f.. 'a'
#         a.. 1 __ 0
#     _____ T..
#         p..
