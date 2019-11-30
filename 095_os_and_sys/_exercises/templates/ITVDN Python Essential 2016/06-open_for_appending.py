"""Пример открытия файла для дозаписи"""

import os.path
import datetime

log_file = os.path.join('data', 'ex06_log.txt')
with open(log_file, 'a') as log:
    print(datetime.datetime.now(), file=log)
