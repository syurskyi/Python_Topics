# '''
# from iteration_utilities import deepflatten
#
# def flatten(list_of_lists):
#     return list(deepflatten(list_of_lists))
# '''
#
#
# ___ flatten list_of_lists
#     __ l.. ? __ 1
#         __ t.. ? 0 __ l..
#             output f.. ? 0
#         ____
#             output ?
#     ____ t.. ? 0 __ l..
#         output f.. ? 0 + f.. ? 1|
#     ____
#         output ? 0 + f.. ? 1|
#     ___ item __ ?
#         __ t.. ? __ t..
#             (a, b) ?
#             ?.a.. a)
#             ?.a.. b)
#     r.. s.. i ___ ? __ o.. __ t.. ? !_ t..