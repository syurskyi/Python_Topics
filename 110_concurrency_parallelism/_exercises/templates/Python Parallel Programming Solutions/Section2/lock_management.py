# ______ th..
#
# shared_resource_with_lock     _ 0
# shared_resource_with_no_lock     _ 0
# COUNT _ 100000
# shared_resource_lock _ ?.L..
#
#
# ####LOCK MANAGEMENT##
# ___ increment_with_lock
#     g.. shared_resource_with_lock
#     ___ i __ ra.. C..
#         _l__.a..
#         ? +_ 1
#         _l__.r..
#
# ___ decrement_with_lock
#     g.. shared_resource_with_lock
#     ___ i __ ra.. C..
#         _l__.a..
#         ? -_ 1
#         _l__.r..
#
# ####NO LOCK MANAGEMENT ##
# ___ increment_without_lock
#     g.. shared_resource_with_no_lock
#     ___ i __ ra.. C..
#         ? +_ 1
#
# ___ decrement_without_lock
#     g.. shared_resource_with_no_lock
#     ___ i __ ra.. C..
#         ? -_ 1
#
# ####the Main program
# __ _______ __ _______
#     t1 _ ?.T..(t.. _ i..
#     t2 _ ?.T..(t.. _ d..
#     t3 _ ?.T..(t.. _ i..
#     t4 _ ?.T..(t.. _ d..
#     _1.s..
#     _2.s..
#     _3.s..
#     _4.s..
#     _1.r..
#     _2.r..
#     _3.r..
#     _4.r..
#     print ("the value of shared variable with lock management is @"\
#            ?
#     print ("the value of shared variable with race condition is @"\
#            ?
#
