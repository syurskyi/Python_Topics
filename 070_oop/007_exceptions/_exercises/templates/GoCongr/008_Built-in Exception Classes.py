# -*- coding: utf-8 -*-

# Built-in Exception Classes
try:
    x = 1 / 0                       # Ошибка: деление на 0
except ArithmeticError:             # Указываем базовый класс
    print("Обработали деление на 0")