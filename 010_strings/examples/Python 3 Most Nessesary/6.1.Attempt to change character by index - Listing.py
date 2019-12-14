# -*- coding: utf-8 -*-

s = "Python"
print(s[0])                    # Можно получить символ по индексу
# 'P'
# s[0] = "J"              # Изменить строку нельзя
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     s[0] = "J"              # Изменить строку нельзя
# TypeError: 'str' object does not support item assignment
#
print(type("строка"))
# <class 'str'>
# print("строка".encode(encoding="cp1251"))
# b'\xf1\xf2\xf0\xee\xea\xe0'
# "строка".encode(encoding="utf-8")
# b'\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0'
#
#
s = bytes("стр str", "cp1251")
# print(s[0], s[5], s[0:3], s[4:7])
# (241, 116, b'\xf1\xf2\xf0', b'str')
print(s)
# b'\xf1\xf2\xf0 str'
#
#
# >>> len("строка")
# 6
# >>> len(bytes("строка", "cp1251"))
# 6
# >>> len(bytes("строка", "utf-8"))
# 12
#
#
# >>> s = bytearray("str", "cp1251")
# >>> s[0] = 49; s               # Можно изменить символ
# bytearray(b'1tr')
# >>> s.append(55); s            # Можно добавить символ
# bytearray(b'1tr7')