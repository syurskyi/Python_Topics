# # DEAD LOCK
# ______ t..
#
#
# ___ produce
#     print('Set locking')
#     w__ ?
#         w__ ?
#             print("It's great")
#     print('Locking release!')
#
#
# lock _ ?.R..
#
# task1 _ ?.T... t.._ ?
# task2 _ ?.T... t.._ ?
#
# _1.s..
# _2.s..
#
# _1.j..
# _2.j..
