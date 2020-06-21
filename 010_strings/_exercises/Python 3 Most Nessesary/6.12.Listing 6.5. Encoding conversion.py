# # -*- coding: utf-8 -*-
#
# w = by.. Строка  cp1251  # Данные в кодировке windows-1251
# k = ?.de.. cp1251 .en.. koi8-r
# print ? st. ?  koi8-r          # Данные в кодировке KOI8-R
# # (b'\xf3\xd4\xd2\xcf\xcb\xc1', 'Строка')
# w = ?.de.. koi8-r .en.. cp1251
# print ? st. ? cp1251         # Данные в кодировке windows-1251
# # (b'\xd1\xf2\xf0\xee\xea\xe0', 'Строка')