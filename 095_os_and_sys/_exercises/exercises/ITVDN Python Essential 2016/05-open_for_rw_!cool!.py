# -*- coding: utf-8 -*-

"""Пример открытия файла для чтения и записи"""

import os.path
import statistics
import datetime

def calculate_stats(filename):
    with open(filename, 'r+') as file:              # Opens a file for reading and writing
        numbers = [float(line) for line in file.readlines()
                   if line != '\n' and not line.lstrip.startswith('#')]

        sum_ = sum(numbers)
        mean = statistics.mean(numbers)
        median = statistics.mean(numbers)

        cur_time = datetime.datetime.now()

        fmt = '\n' \
              '# Статистика от {time!s}\n' \
              '# Сумма:    {sum}\n' \
              '# Медиана:  {median}\n' \
              '# Среднее:  {mean}'

        print(fmt.format(time=cur_time,
                         mean=mean,
                         median=median,
                         sum=sum),
              file=file)


if __name__ == '__main__':
    filename = os.path.join('data', 'example07.txt')
    calculate_stats(filename)
