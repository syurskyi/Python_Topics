# #Synchronize processes with barrier – Chapter 3: Process Based Parallelism
#
# ______ m..
# ____ m.. ______ B.. L.. P..
# ____ ti.. ______ ti..
# ____ d_t_ ______ d_t_
#
#
# ___ test_with_barrier synchronizer serializer
#     name _ ?.c_p.. .n..
#     ?.w..
#     now _ t__
#     w__ ?:
#         print("process @ ----> @" \
#               n.. d_t_.f_t_s.. n..
#
# ___ test_without_barrier():
#     name _ ?.c_p.. .name
#     now _ t__()
#     print("process @ ----> @" \
#           @(name ,d_t_.f_t_s.. n..
#
# __ _______ __ _______
#     synchronizer _ B.. 2
#     serializer _ L..
#     P.. n.._'p1 - test_with_barrier'\
#             t..? \
#             a.._ ? ? .s..
#     P.. n.._'p2 - test_with_barrier'\
#             ,t..? \
#             a.._ ? ? .s..
#     P.. n.._'p3 - test_without_barrier'\
#             t..? .s..
#     P.. n.._'p4 - test_without_barrier'\
#             t..? .s..

