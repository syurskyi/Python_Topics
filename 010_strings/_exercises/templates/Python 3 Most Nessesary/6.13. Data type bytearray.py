# # -*- coding: utf-8 -*-
#
# print b_a_
# # bytearray(b'')
# print b_a_ строка  cp1251
# # bytearray(b'\xf1\xf2\xf0\xee\xea\xe0')
# # print(bytearray("строка"))
# # Traceback (most recent call last):
# #   File "<pyshell#2>", line 1, in <module>
# #     bytearray("строка")
# # TypeError: string argument without an encoding
#
#
# # print(bytearray("string\uFFFD", "cp1251", "strict"))
# # Traceback (most recent call last):
# #   File "<pyshell#5>", line 1, in <module>
# #     bytearray("string\uFFFD", "cp1251", "strict")
# #   File "C:\Python34\lib\encodings\cp1251.py", line 12, in encode
# #     return codecs.charmap_encode(input,errors,encoding_table)
# # UnicodeEncodeError: 'charmap' codec can't encode character
# # '\ufffd' in position 6: character maps to <undefined>
# print b_a_ string\uFFFD  cp1251  r..
# # bytearray(b'string?')
# print b_a_ string\uFFFD cp1251  i..
# # bytearray(b'string')
#
#
# b = b_a_ 225, 226, 224, 174, 170, 160
# print ?
# # bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0')
# print b_a_ _'\xe1\xe2\xe0\xae\xaa\xa0'
# # bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0')
# print st. ? cp866
# # 'строка'
#
#
# print b_a_ 5
# # bytearray(b'\x00\x00\x00\x00\x00')
#
#
# b = b_a_.f_h_" e1 e2e0ae aaa0 "
# print ?
# # bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0')
# print st. ? cp866
# # 'строка'
#
#
# b = b_a_ Python ascii
# print ? 0                           # Можем получить значение
# # 80
# ? 0 = _"J" 0                   # Можем изменить значение
# print ?
# # bytearray(b'Jython')
#
#
# b = b_a_ string  ascii
# ?.ap.. _"1" 0 print ?
# # bytearray(b'string1')
#
#
# b = b_a_("string", "ascii")
# b.extend(b"123"); print ?
# # bytearray(b'string123')
#
#
# b = b_a_ string ascii
# ? + _"123"                  # Возвращает новый объект
# # bytearray(b'string123')
# ? += _"456"; print ?             # Изменяет текущий объект
# # bytearray(b'string456')
#
#
# b = b_a_ string ascii
# ? le. ? _ _"123"         # Добавляем элементы в последовательность
# print ?
# # bytearray(b'string123')
#
#
# b = b_a_ string  ascii
# ?.in.. 0; _"1" 0 print ?
# # bytearray(b'1string')
#
#
# b = b_a_ string  ascii
# b ;0 _ _"123"; print ?
# # bytearray(b'123string')
#
#
# b _ b_a_ string  ascii
# print ?.p..               # Удаляем последний элемент
# # 103
# print ?
# # bytearray(b'strin')
# print ?.p.. 0               # Удаляем первый элемент
# # 115
# print ?
# # bytearray(b'trin')
#
#
# b = b_a_ string  ascii
# del ? 5             # Удаляем последний элемент
# print ?
# # bytearray(b'strin')
# del ? ;2            # Удаляем первый и второй элементы
# print ?
# # bytearray(b'rin')
#
#
# b = b_a_ strstr ascii
# ?.re.. _"s" 0     # Удаляет только первый элемент
# print ?
# # bytearray(b'trstr')
#
#
# b = b_a_ string   ascii
# # print(b.reverse(); b)
# # bytearray(b'gnirts')
#
#
# b = b_a_ строка  cp1251
# print ?.de.. en.._cp1251, ?.de.. cp1251
# # ('строка', 'строка')
#
#
# b = b_a_ строка  cp1251
# print st. ? cp1251
# # 'строка'