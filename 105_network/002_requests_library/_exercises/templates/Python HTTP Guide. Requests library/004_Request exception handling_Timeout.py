# В requests имеется 2 вида таймаут-исключений:
#
#     ConnectTimeout - таймаут на соединения
#     ReadTimeout - таймаут на чтение

______ r__
try:
    response = ?.g..('https://httpbin.org/user-agent', timeout=(0.00001, 10))
except ?.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')

# Oops. Connection timeout occured!
try:
    response = ?.g..('https://httpbin.org/user-agent', timeout=(10, 0.0001))
except ?.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except ?.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')

# Oops. Read timeout occured