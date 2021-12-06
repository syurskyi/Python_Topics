# _______ c__.f__
# _______ _
# _______ t___
#
#
# c_ BankAccount
#     ___  -
#         balance = 100  # shared data/resource
#         lock_obj = _.L..
#
#     ___ update transaction amount
#         print _*|t.. started
#
#         w___ lock_obj
#             tmp_amount = b..
#             tmp_amount += a..
#             t___.s 1
#             b.. = ?
#
#         print _*|t.. ended
#
#
# __ _____ __ _____
#     # lock_obj = threading.Lock()
#     # print(lock_obj.locked())
#     #
#     # lock_obj.acquire()
#     # print(lock_obj.locked())
#     #
#     # lock_obj.release()
#     # print(lock_obj.locked())
#
#     acc = ?
#     print _*Main started. acc.balance=|?.b..
#
#     w___ c__.f__.T... m.._2 __ ex
#         ?.m.. ?.u.. ('refill', 'withdraw'), (100, -200))
#
#     print _*End of main. Balance= |?.b..
