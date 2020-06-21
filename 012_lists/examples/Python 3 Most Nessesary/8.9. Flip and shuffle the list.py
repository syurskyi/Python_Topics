# -*- coding: utf-8 -*-

arr = [1, 2, 3, 4, 5]
arr.reverse()                           # Изменяется текущий список
print(arr)
# [5, 4, 3, 2, 1]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reversed(arr))
# <list_reverseiterator object at 0x00FD5150>
print(list(reversed(arr)))              # Использование функции list()
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in reversed(arr):
    print(i, end=" ")                   # Вывод с помощью цикла

# 10 9 8 7 6 5 4 3 2 1
print([i for i in reversed(arr)])              # Использование генератора списков
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


import random                           # Подключаем модуль random
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(arr)                      # Перемешиваем список случайным образом
print(arr)
# [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
