# _______ _
# _______ t___
#
# a = 5
# b = 5
#
# a_lock = _.L..
# b_lock = _.L..
#
#
# ___ thread1calc
#     g___ a
#     g___ b
#
#     print('Thread1 acquiring lock a')
#     ?.a..
#     t___.s.. 5
#
#     print('Thread1 acquiring lock b')
#     ?.a..
#     t___.s.. 5
#
#     a += 5
#     b += 5
#
#     print('Thread1 releasing both locks')
#     ?.r..
#     ?.r..
#
#
# ___ thread2calcg___
#     g___ a
#     g___ b
#
#     print('Thread2 acquiring lock b')
#     ?.a..
#     t___.s.. 5
#
#     print('Thread2 acquiring lock a')
#     ?.a..
#     t___.s.. 5
#
#     a += 10
#     b += 10
#
#     print('Thread2 releasing both locks')
#     ?.r..
#     ?.r..
#
#
# __ _____ __ _____
#     t1 = _.T..(t.._?
#     ?.s....
#
#     t2 = _.T..(t.._?
#     ?.s..