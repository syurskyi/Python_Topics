# # -*- coding: utf-8 -*-

import os                      # Подключаем модуль os
print(os.access(r"file.txt", os.F_OK))  # Файл существует
# True
print(os.access(r"C:\book", os.F_OK))  # Каталог существует
# True
print(os.access(r"C:\book2", os.F_OK))  # Каталог не существует
# False

# __.c.m. _ file.txt 0o777  # Полный доступ к файлу
