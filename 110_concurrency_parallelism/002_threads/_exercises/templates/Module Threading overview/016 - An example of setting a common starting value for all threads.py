# _____ _ r__
#
#
# ___ show_value data
#     name_thread  _.c...n..
#     ___
#         val  ?.v..
#     _____ A..
#         print _* ? : Нет локального значения value
#     ____
#         print _* ?: value= ?
#
#
# ___ worker data
#     name_thread  _.c...n..
#     ? ?
#     print _* ?: установка локального value
#     ?.v..  r__.r.. 1 100
#     ? ?
#
#
# c_ MyLocal _.l..
#     # !!! переопределяем конструктор класса
#     ___  -  value
#         s.. . -
#         ?  ?
#         n.. =_.c...n..
#         print _* n.. стартовое значение ?
#
#
# local_data  ? 1000
# ? ?
#
# ___ i __ r.. 2
#     t  _.? t.. ? a.. ?
#     ?.s..
#
# # MainThread стартовое значение 1000
# # MainThread: value=1000
# # Thread-1 стартовое значение 1000
# # Thread-1: value=1000
# # Thread-1: установка локального value
# # Thread-1: value=31
# # Thread-2 стартовое значение 1000
# # Thread-2: value=1000
# # Thread-2: установка локального value
# # Thread-2: value=69