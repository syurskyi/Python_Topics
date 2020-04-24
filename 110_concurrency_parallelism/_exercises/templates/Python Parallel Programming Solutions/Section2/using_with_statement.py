# ______ th..
# ______ lo..
#
# ?.b.. l.._?.D..
#                     f.._'|@|tN..-10_| @|m.. _',)
#
# ___ threading_with statement
#     w__ ?
#         ?.d.. '@ acquired via with' ?
#
# ___ threading_not_with( tatement
#     ?.a..
#     ___
#         ?.d.. '@ acquired directly' ?
#     f..
#         ?.r..
#
# __ _______ __ _______
#
# #let's create a test battery
#     lock _ ?.L..
#     rlock _ ?.RL..
#     condition _ ?.C..
#     mutex _ ?.S.. 1
#     threading_synchronization_list _ |? ? ? ?
#
# #in the for cycle we call the threading_with e threading_no_with function
#     ___ s.. __ t_s_l..
#         t1 _ ?.T.. t.._t_w.. a.._ s..
#         t2 _ ?.T.. t.._t_n_w.. a.._ s..
#         _1.s..
#         _2.s..
#         _1.r..
#         _2.r..
