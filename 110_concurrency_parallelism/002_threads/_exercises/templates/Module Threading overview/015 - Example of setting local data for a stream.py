# _____ _ r__
#
#
# ___ show_value data
#     name_thread = _.c...n..
#     ___
#         val = ?.v..
#     _____ A..
#         print _* ? Нет локального значения value
#     ____
#         print _*?: value= ?
#
#
# ___ worker data
#     name_thread = _.c...n..
#     show_value ?
#     print _*Установка значения value для потока ?
#     ?.v.. = r__.r.. 1 100
#     ? ?
#
#
# local_data = _.l...
# ? ?
# # установка значения value для
# # основного потока программы
# ?.v.. = 1000
# ? ?
#
# ___ i __ r.. 2
#     t = _.? t.. ? a.. ?
#     ?.s..
#
# # MainThread: Нет локального значения value
# # MainThread: value=1000
# # Thread-1: Нет локального значения value
# # Установка значения value для потока Thread-1.
# # Thread-1: value=63
# # Thread-2: Нет локального значения value
# # Установка значения value для потока Thread-2.
# # Thread-2: value=35