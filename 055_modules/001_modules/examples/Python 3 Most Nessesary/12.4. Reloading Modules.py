from imp import reload
reload(<Объект модуля>)


# -*- coding: utf-8 -*-
x = 150


import sys
sys.path.append(r"C:\book") # Добавляем путь к папке с модулем
import tests2               # Подключаем модуль tests2.py
print(tests2.x)             # Выводим текущее значение
# 150


# Изменяем значение в модуле на 800
import tests2
print(tests2.x)             # Значение не изменилось
# 150
