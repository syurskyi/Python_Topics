# # ch12/example1.py
#
# ______ th..
# ______ ti..
#
# ___ thread_a
#     print('? A is starting...')
#
#     print('? A waiting to acquire lock A.')
#     lock_a.a..
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
#     print('? B waiting to acquire lock B.')
#     _b.a..
#     print('? B has acquired lock B, performing some calculation...')
#     t__.s.. 5
#
#     print('? B waiting to acquire lock A.')
#     _a.a..
#     print('? B has acquired lock A, performing some calculation...')
#     t__.s..5
#
#     print('? B releasing both locks.')
#     lock_b.r..
#     lock_a.r..
#
# lock_a _ ?.L..
# lock_b _ ?.L..
#
# thread1 _ ?.T..(t.._?_a)
# thread2 _ ?.T..(t.._?_b)
#
# _1.s..
# _2.s..
#
# _1.j..
# _2.j..
#
# print('Finished.')
