# # DEAD LOCK
# ______ ...
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
# # __enter__ => ?.a..
# # __exit__ => ?.r..
#
# task1 = ?.T.. t.._?
# task2 = ?.T.. t.._?
#
# ?.s..
# ?.s..
#
# ?.j..
# ?.j..
