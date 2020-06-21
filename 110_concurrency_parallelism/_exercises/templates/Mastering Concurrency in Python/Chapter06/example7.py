# # ch6/example7.py
#
# ____ ma__ ______ sqrt
# ______ m..
#
# c_ Consumer ?.P..
#
#     ___  -  task_queue result_queue
#         ?.P... - ?
#         ? ?
#         ? ?
#
#     ___ run
#         pname _ name
#
#         w__ no. t__.e..
#
#             temp_task _ t__.g..
#
#             print('@ processing task: @' p..  ?
#
#             answer _ ?.p..
#             t_q_.t_d..
#             r_q_.p.. ?
#
# c_ Task
#     ___  -  x
#         ? ?
#
#     ___ process
#         __ ? < 2
#             r_ '@ is not a prime number.'  ?
#
#         __ ? __ 2
#             r_ '@ is a prime number.'  ?
#
#         __ ?  2 __ 0
#             r_ '@ is not a prime number.'  ?
#
#         limit _ in. sq.. ?|| + 1
#         ___ i __ ra.. 3 ? 2
#             __ ?  i __ 0
#                 r_ '@ is not a prime number.'  ?
#
#         r_ '@ is a prime number.'  ?
#
#     ___ -s
#         r_ 'Checking if @ is a prime or not.'  ?
#
# __ _______ __ _______
#
#     tasks _ ?.JQ..
#     results _ ?.Q..
#
#     # spawning consumers with respect to the
#     # number cores available in the system
#     n_consumers _ ?.c_c..
#     print('Spawning @ consumers...'  n_
#     consumers _ C.. t.. r..| ___ i __ ra.. n_
#     ___ consumer __ ?
#         ?.s..
#
#     # enqueueing jobs
#     my_input _ [2, 36, 101, 193, 323, 513, 1327, 100000, 9999999, 433785907]
#     ___ item __ ?
#         ?s.p.. T.. ?
#
#     ?s.j..
#
#     ___ i __ ra.. le. ?
#         temp_result _ r__.g..
#         print('Result:' ?
#
#     print('Done.')
