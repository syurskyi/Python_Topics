# ______ th..
# ______ ti..
# ____ t_i_ ______ d_t_ __ timer
#
# ___ thread_a
#     print('? A is starting...')
#
#     print('? A waiting to acquire lock A.')
#     _a.a..
#     print('? A has acquired lock A, performing some calculation...')
#     t__.s.. 2
#
#     print('? A waiting to acquire lock B.')
#     lock_b.a..
#     print('? A has acquired lock B, performing some calculation...')
#     t__.s.. 2
#
#     print('? A releasing both locks.')
#     _a.r..
#     _b.r..
#
# ___ thread_b
#     print('? B is starting...')
#
#     print('? B waiting to acquire lock A.')
#     _a.a..
#     print('? B has acquired lock A, performing some calculation...')
#     t__.s.. 5
#
#     print('? B waiting to acquire lock B.')
#     _b.a..
#     print('? B has acquired lock B, performing some calculation...')
#     t__.s.. 5
#
#     print('? B releasing both locks.')
#     _b.r..
#     _a.r..
#
# lock_a _ ?.L..
# lock_b _ ?.L..
#
# thread1 _ ?.T.. t.._?_a
# thread2 _ ?.T.. t.._?_b
#
# start _ ti..
#
# _1.s..
# _1.j..
#
# _2.s..
# _2.j..
#
# print('Took @.2_ seconds.'  t.. - s..
# print('Finished.')
