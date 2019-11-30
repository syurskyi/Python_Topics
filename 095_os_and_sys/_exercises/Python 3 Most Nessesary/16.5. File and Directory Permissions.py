# # -*- coding: utf-8 -*-

import os                       # Подключаем модуль os
os.access(r"file.txt", os.F_OK)  # Файл существует
# True
os.access(r"C:\book", os.F_OK)  # Каталог существует
# True
os.access(r"C:\book2", os.F_OK)  # Каталог не существует
# False

os.chmod(r"file.txt", 0o777)  # Полный доступ к файлу
