# -*- coding: utf-8 -*-

"""Пример перезаписи файла"""

import os.path

filename = os.path.join('data', 'example07.txt')

# Чтение файла
with open(filename, 'r') as file:
    lines = file.readlines()

# Модификация данных
lines.insert(2, 'inserted line\n')

# Перезапись файла
with open(filename, 'a') as file:
    file.writelines(lines)
