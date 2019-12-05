# -*- coding: utf-8 -*-

# Processing division by zero

try:                               # Перехватываем исключения
    x = 1 / 0                      # Ошибка: деление на 0
except ZeroDivisionError:          # Указываем класс исключения
    print("Обработали деление на 0")
    x = 0
print(x)                           # Выведет: 0