# ##Using Pipes with multiprocessing – Section 3: Process Based Parallelism
#
# ______ m..
#
#
# ___ create_items pipe
#     output_pipe, _ _ ?
#     ___ item __ ra.. 10
#         o__.s.. ?
#     o__.c..
#
# ___ multiply_items pipe_1, pipe_2
#     close, input_pipe _ pipe_1
#     c__.c..
#     o.., _ _ pipe_2
#     ___
#         w__ T..
#             item _ i__.r..
#             o__.s.. i.. * i..
#     e___ E..
#         o___.c..
#
#
# __ _______ __ _______
#
# #First process pipe with numbers from 0 to 9
#     pipe_1 _ ?.P.. T..
#     process_pipe_1 _ \
#                    ?.P..\
#                    |t.._c.. a.._ _1
#     ?.s..
#
# #second pipe,
#     pipe_2 _ ?.P.. T..
#     process_pipe_2 _ \
#                    ?.P..\
#                     t.._m.. a.._ _1 _2
#     ?.s..
#
#     _1 0 .c..
#     _2 0 .c..
#
#     ___
#         w__ T..
#
#             print _2 1.r..
#     _______ E..
#         print ("End")
