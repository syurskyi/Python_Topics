# _____ _ t__
#
# ___ wait_event
#     print('Старт WAIT_EVENT()')
#     e__.w..
#     print('Код обработки по событию в WAIT_EVENT()')
#
# ___ wait_timeout time_out
#     print('Старт WAIT_TIMEOUT() ')
#     w__ n__ e__.i..
#         is_set = e__.w.. t.. ?
#         print _* TimeOut ? секунды истек
#         __ ?
#             print('Код обработки по событию в WAIT_TIMEOUT()')
#         ____
#             print('Пока ждем события, код обработки чего-то другого')
#             t__.s.. 3
#
# # установка глобального события
# event = _.?
#
# t1 = _.? n.. 'blocking',
#                   t.. ?
# ?.s..
#
# t2 = _.? n.. non-blocking
#                   t.. ?
#                   a.. 2
# ?.s..
#
# print('Ожидание перед вызовом Event.set()')
# t__.s.. 5
# ?.s..
# print('Установлено событие в основном потоке')
#
#
# # Старт WAIT_EVENT()
# # Старт WAIT_TIMEOUT()
# # Ожидание перед вызовом Event.set()
# # TimeOut 2 секунды истек
# # Пока ждем события, код обработки чего-то другого
# # Установлено событие в основном потоке
# # Код обработки по событию в WAIT_EVENT()
# # TimeOut 2 секунды истек
# # Код обработки по событию в WAIT_TIMEOUT()