# # genmulti.py
# #
# # Generate items from multiple generators (multiplex)
# #
#
# ______ qu___, t___
# f.. genqueue ______ genfrom_queue, sendto_queue
# f.. gencat ______ gen_cat
#
# ___ multiplex sources
#     in_q _ qu___.Q..
#     consumers _ # list
# # src
#     ___ ? __ ?
#         thr _ t___.T... t.._s..
#                                a.._(?, i..
#         ?.s..
#         c__.ap.. g.. i..
#     r_ g.. c..
#
# ___ gen_multiplex genlist
#     item_q _ qu___.Q..
#     ___ run_one source
# # item
#         ___ ? __ ?
#             i__.p.. ?
#
#     ___ run_all
#         thrlist _ # list
# # source
#         ___ ? __ ?
#             t _ t___.T... t.._r.. a.._ s..
#             ?.s..
#             t__.ap.. ?
#         ___ t __ t..
#             ?.j..
#         i__.p.. S_I..
#
#     t___.T... t.._r_a__ .s..
#     w____ T..
#         item _ i__.g..
#         __ ? __ S_I_
#             r_
#         y... ?
#
#
# # Example use
# #
# # This example requires you to perform these setup steps:
# #
# # 1.  Go to run/foo and run logsim.py
# # 2.  Go to run/bar and run logsim.py
# #
# # These two steps will start writing two different Apache log files.
# # Now, we're going to read from both at the same time.
#
# __ __name__ __ '__main__':
#     f.. follow ______ follow
#
#     log1 _ f.. o.. *run/foo/access-log
#     log2 _ f.. o.. *run/bar/access-log
#
#     log _ m.. ? ?
#     # line
#     ___ ? __ ?
#         print ? e.._''
