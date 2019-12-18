# -*- coding: utf-8 -*-

w = bytes("Строка", "cp1251")  # Данные в кодировке windows-1251
k = w.decode("cp1251").encode("koi8-r")
print(k, str(k, "koi8-r"))           # Данные в кодировке KOI8-R
# (b'\xf3\xd4\xd2\xcf\xcb\xc1', 'Строка')
w = k.decode("koi8-r").encode("cp1251")
print(w, str(w, "cp1251") )          # Данные в кодировке windows-1251
# (b'\xd1\xf2\xf0\xee\xea\xe0', 'Строка')