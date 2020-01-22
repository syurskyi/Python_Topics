# # The Context Management Protocol
# c_ TraceBlock
#     ___ message ____  arg
#         print('running' ?
#     ___ -e
#         print('starting with block')
#         r_ ____
#     ___ -e ____,__ __
#         __ e._t. __ N..
#             print('exited normally\n')
#         _____
#             print('raise an exception!', e._t.
#             r_ F..                                  # Propagate
#
# ____ ? __ action
#     ?.m.. test 1'
#     print('reached')
#
# ___ ? __ action
#     ?.m..('test 2')
#     r____ T..
#     print('not reached')
