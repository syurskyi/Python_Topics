# # -*- coding: utf-8 -*-
#
# print by..
# # b''
# print(by строка cp1251
# # b'\xf1\xf2\xf0\xee\xea\xe0'
# # print(bytes("строка"))
# # Traceback (most recent call last):
# #   File "<pyshell#33>", line 1, in <module>
# #     bytes("строка")
# # TypeError: string argument without an encoding
#
#
# # print(bytes("string\uFFFD", "cp1251", "strict"))
# # Traceback (most recent call last):
# #   File "<pyshell#35>", line 1, in <module>
# #     bytes("string\uFFFD", "cp1251", "strict")
# #   File "C:\Python34\lib\encodings\cp1251.py", line 12, in encode
# #     return codecs.charmap_encode(input,errors,encoding_table)
# # UnicodeEncodeError: 'charmap' codec can't encode character
# # '\ufffd' in position 6: character maps to <undefined>
# print by..  string\uFFFD cp1251 r..
# # b'string?'
# print by.. string\uFFFD cp1251  ignore
# # b'string'
#
#
# print строка".en..
# # b'\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0'
# # print("стро.encode(encoding="cp1251"))
# # b'\xf1\xf2\xf0\xee\xea\xe0'
# print строка\uFFFD".en.. en.._ cp1251
#                             er.._ xmlcharrefreplace
# # b'\xf1\xf2\xf0\xee\xea\xe0&#65533;'ка"
# print строка\uFFFD .en.. en.._"cp1251",
#                             er.._ backslashreplace
# # b'\xf1\xf2\xf0\xee\xea\xe0\\ufffd'
#
#
# print(b"string", b'string', b"""string""", b'''string''')
# # (b'string', b'string', b'string', b'string')
# # print(b"строка")
# # SyntaxError: bytes can only contain ASCII literal characters.
# print(b"\xf1\xf2\xf0\xee\xea\xe0")
# # b'\xf1\xf2\xf0\xee\xea\xe0'
#
#
# b = by.. 225, 226, 224, 174, 170, 160
# print ?
# # b'\xe1\xe2\xe0\xae\xaa\xa0'
# print st. ? cp866
# # 'строка'
#
#
# print by..10
# # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#
#
# b = by__.f.h." e1 e2e0ae aaa0 "
# print ?
# # b'\xe1\xe2\xe0\xae\xaa\xa0'
# print st. ? "cp866"
# # 'строка'
#
#
# b = by.. string cp1251
# print ?
# # b'string'
# print ? 0                      # Обращение по индексу
# # 115
# print ? 1 3                      # Получение среза
# # b'tr'
# print ? + _"123"                 # Конкатенация
# # b'string123'
# print(b * 3)                    # Повторение
# # b'stringstringstring'
# print(115 in b, b"tr" in b, b"as" in b)
# # (True, True, False)
#
#
# print li.. by.. string  cp1251
# # [115, 116, 114, 105, 110, 103]
#
#
# b = by.. string  cp1251
# # b[0] = 168
# # Traceback (most recent call last):
# #   File "<pyshell#76>", line 1, in <module>
# #     b[0] = 168
# # TypeError: 'bytes' object does not support item assignment
#
#
# b = by.. string  cp125
# print ?.re.. _"s" _"S"
# # b'String'
#
#
# # print(b"string" + "string")
# # Traceback (most recent call last):
# #   File "<pyshell#79>", line 1, in <module>
# #     b"string" + "string"
# # TypeError: can't concat bytes to str
# print _"string" + "string".en.. ascii
# # b'stringstring'
#
#
# print l.. строка
# # 6
# print le. by.. строка cp1251
# # 6
# print le. by.. строка utf-8
# # 12
#
#
# b = by.. строка  cp1251
# print ?.de.. en.._cp1251 ?.de.. cp1251
# # ('строка', 'строка')
#
#
# b = by.. строка  cp1251
# print st.  ? cp1251
# # 'строка'