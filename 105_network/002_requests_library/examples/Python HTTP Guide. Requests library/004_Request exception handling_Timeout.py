# В requests имеется 2 вида таймаут-исключений:
#
#     ConnectTimeout - таймаут на соединения
#     ReadTimeout - таймаут на чтение

import requests
try:
    response = requests.get('https://httpbin.org/user-agent', timeout=(0.00001, 10))
except requests.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')

# Oops. Connection timeout occured!
try:
    response = requests.get('https://httpbin.org/user-agent', timeout=(10, 0.0001))
except requests.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
except requests.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')

# Oops. Read timeout occured