# # В requests имеется 2 вида таймаут-исключений:
# #
# #     ConnectTimeout - таймаут на соединения
# #     ReadTimeout - таймаут на чтение
#
# ______ r__
# ___
#     response _ ?.g..('https://httpbin.org/user-agent', t.._(0.00001, 10))
# _____ ?.e__.CT..
#     print('Oops. Connection timeout occured!')
#
# # Oops. Connection timeout occured!
# ___
#     response _ ?.g.. 'https://httpbin.org/user-agent' t.._(10, 0.0001
# _____ ?.e__.RT..
#     print('Oops. Read timeout occured')
# _____ ?.e__.CT..
#     print('Oops. Connection timeout occured!')
#
# # Oops. Read timeout occured