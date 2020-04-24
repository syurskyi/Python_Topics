# ##Using Queue with multiprocessing – Section 3: Process Based Parallelism
#
# ______ m..
# ______ ra__
# ______ t__
#
# c_ producer ?.P..
#     ___  - queue
#         ?.P.. . -
#         ? ?
#
#     ___ run
#         ___ i __ ra.. 10
#             item _ ra__.r_i.. 0, 256
#             q__.p.. ?
#             print ("P.. Producer : item @d appended to queue @"\
#                    i.. n..
#             t__.s.. 1
#             print ("The size of queue is @"\
#                     q__.qs..
#
# c_ consumer ?.P..
#     ___  -  queue
#         ?.P.. . -
#         ? ?
#
#     ___ run
#         w__ T..
#             __ q__.e..
#                 print("the queue is empty")
#             ____
#                 t__.s.. 2
#                 item _ q__.g..
#                 print ('P.. Consumer : item @d popped from by @ \n'\
#                         i.. n..
#                 t__.s.. 1
#
#
# __ _______ __ _______
#         queue _ ?.Q..
#         process_producer _ ? ?
#         process_consumer _ ? ?
#         _p__.s..
#         _c__.s..
#         _p__.r..
#         _c__.r..
