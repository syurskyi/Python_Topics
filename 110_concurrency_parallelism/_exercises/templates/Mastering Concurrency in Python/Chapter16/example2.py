# # ch16/example2.py
#
# ______ th..
# ____ c__.f.. ______ TPE..
# ______ ti..
#
# c_ LockedCounter
#     ___  -
#         value _ 0
#         lock _ ?.L..
#
#     ___ increment x
#         w__ l..
#             new_value _ v.. + ?
#             t__.s.. 0.001 # creating a delay
#             value _ ?
#
#     ___ get_value
#         w__ l..
#             ? _ ?
#
#         r_ ?
#
# counter _ LoC..
# w__ TPE.. m.._3 __ executor
#     ?.m.. c__.i.. 1 ___ i __ ra.. 300
#
# print _*Final counter: |c_.g_v.. .
# print('Finished.')
