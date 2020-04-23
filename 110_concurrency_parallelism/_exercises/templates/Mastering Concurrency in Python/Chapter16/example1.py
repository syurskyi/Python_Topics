# # ch16/example1.py
#
# ____ c__.f.. ______ TPE..
# ______ ti..
#
# c_ LocklessCounter
#     ___  -
#         value _ 0
#
#     ___ increment x
#         new_value _ v.. + x
#         t__.s.. 0.001 # creating a delay
#         value _ ?
#
#     ___ get_value
#         r_ ?
#
# counter _ ?
# w__ TPE.. m.._3 __ executor
#     ?.m.. c__.i.. |1 ___ i __ ra.. 300
#
# print _*Final counter: |c__.g_v.. .
# print('Finished.')
