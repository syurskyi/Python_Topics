# _____ _ r__ t__
#
#
# c_ ActivePool
#     """Воображаемый пул соединений"""
#
#     start  t__.t__
#
#     ___  -
#         s___ ? _____ -
#         active  # list
#         lock  _.?
#
#     ___ makeActive name
#         w__ ?
#             ?.a.. ?
#             tm  t__.t__ - ?
#             print _*Время: r.. ? 3 Running: ?
#
#     ___ makeInactive name
#         w__ ?
#             ?.r.. ?
#             tm  t__.t__ - ?
#             print _*Время: r..(? 3 Running: ?
#
#
# ___ worker sem pool
#     w__ ?
#         th_name  _.c...n..
#         print _* ? ожидает присоединения к пулу
#         ?.m.. ?
#         t__.s.. 0.5
#         ?.m.. ?
#
#
# # переменная семафора
# sem  _.? 2
#
# # воображаемый пул соединений
# pool  ?
# # запускаем потоки
# ___ i __ r..4
#     t  _.?
#         t.. ?
#         a.. ? ?
#
#     ?.s..
#
# # Thread-1 ожидает присоединения к пулу
# # Время: 0.0 Running: ['Thread-1']
# # Thread-2 ожидает присоединения к пулу
# # Время: 0.0 Running: ['Thread-1', 'Thread-2']
# # Время: 0.501 Running: ['Thread-2']
# # Thread-3 ожидает присоединения к пулу
# # Время: 0.501 Running: []
# # Время: 0.502 Running: ['Thread-3']
# # Thread-4 ожидает присоединения к пулу
# # Время: 0.502 Running: ['Thread-3', 'Thread-4']
# # Время: 1.003 Running: ['Thread-4']
# # Время: 1.003 Running: []