# # DEAD LOCK
# ______ t..
#
#
# ___ producer
#     print('Set locking')
#     w__ ?
#         print('done')
#         w__ ?
#             print("It's great")
#     print('Locking release!')
#
#
# lock _ ?.L..
# # __enter__ => lock.a..
# # __exit__ => lock.release()
#
# task1 = ?.T.. t.._?
# task2 = ?.T.. t.._?
#
# _1.s..
# _2.s..
#
# _1.j..
# _2.j..
