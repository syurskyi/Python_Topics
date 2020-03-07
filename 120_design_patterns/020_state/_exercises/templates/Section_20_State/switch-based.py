# ____ en.. ______ E.. a..
#
#
# class State E..
#     LOCKED _ ?
#     FAILED _ ?
#     UNLOCKED _ ?
#
#
# __ ________ __ _______
#     code _ '1234'
#     state _ S___.L..
#     entry _ ''
#
#     w__ T..
#         __ s.. __ S___.L..
#             e.. +_ in.. e..
#
#             __ e.. __ c..
#                 s.. _ S___.U..
#
#             __ no. c___.s_wi.. e..
#                 # the code is wrong
#                 s.. _ S___.F..
#         ____ s... __ S___.F..
#             print('\nFAILED')
#             e.. _ ''
#             s.. _ S___.L...
#         ____ s.. __ S___.U...
#             print('\nUNLOCKED')
#             b..
