# # -*- coding: utf-8 -*-

try:
    open("C:\temp\new\file.txt")
except F..
    print("Файл отсутствует")
except IsADirectoryError:
    print("Это не файл, а папка")
except PermissionError:
    print("Отсутствуют права на доступ к файлу")
except OSError:
    print("Неустановленная ошибка открытия файла")
. . .