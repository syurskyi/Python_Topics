# -*- coding: utf-8 -*-

print(bytearray())
# bytearray(b'')
print(bytearray("строка", "cp1251"))
# bytearray(b'\xf1\xf2\xf0\xee\xea\xe0')
# print(bytearray("строка"))
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     bytearray("строка")
# TypeError: string argument without an encoding


# print(bytearray("string\uFFFD", "cp1251", "strict"))
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     bytearray("string\uFFFD", "cp1251", "strict")
#   File "C:\Python34\lib\encodings\cp1251.py", line 12, in encode
#     return codecs.charmap_encode(input,errors,encoding_table)
# UnicodeEncodeError: 'charmap' codec can't encode character
# '\ufffd' in position 6: character maps to <undefined>
print(bytearray("string\uFFFD", "cp1251", "replace"))
# bytearray(b'string?')
print(bytearray("string\uFFFD", "cp1251", "ignore"))
# bytearray(b'string')


b = bytearray([225, 226, 224, 174, 170, 160])
print(b)
# bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0')
print(bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0'))
# bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0')
print(str(b, "cp866"))
# 'строка'


print(bytearray(5))
# bytearray(b'\x00\x00\x00\x00\x00')


b = bytearray.fromhex(" e1 e2e0ae aaa0 ")
print(b)
# bytearray(b'\xe1\xe2\xe0\xae\xaa\xa0')
print(str(b, "cp866"))
# 'строка'


b = bytearray("Python", "ascii")
print(b[0])                            # Можем получить значение
# 80
b[0] = b"J"[0]                    # Можем изменить значение
print(b)
# bytearray(b'Jython')


b = bytearray("string", "ascii")
b.append(b"1"[0]); b
# bytearray(b'string1')


b = bytearray("string", "ascii")
b.extend(b"123"); b
# bytearray(b'string123')


b = bytearray("string", "ascii")
b + b"123"                  # Возвращает новый объект
# bytearray(b'string123')
b += b"456"; b              # Изменяет текущий объект
# bytearray(b'string456')


b = bytearray("string", "ascii")
b[len(b):] = b"123"         # Добавляем элементы в последовательность
print(b)
# bytearray(b'string123')


b = bytearray("string", "ascii")
b.insert(0, b"1"[0]); b
# bytearray(b'1string')


b = bytearray("string", "ascii")
b[:0] = b"123"; b
# bytearray(b'123string')


b = bytearray("string", "ascii")
print(b.pop())                # Удаляем последний элемент
# 103
print(b)
# bytearray(b'strin')
print(b.pop(0))               # Удаляем первый элемент
# 115
print(b)
# bytearray(b'trin')


b = bytearray("string", "ascii")
del b[5]              # Удаляем последний элемент
print(b)
# bytearray(b'strin')
del b[:2]             # Удаляем первый и второй элементы
print(b)
# bytearray(b'rin')


b = bytearray("strstr", "ascii")
b.remove(b"s"[0])     # Удаляет только первый элемент
print(b)
# bytearray(b'trstr')


b = bytearray("string", "ascii")
# print(b.reverse(); b)
# bytearray(b'gnirts')


b = bytearray("строка", "cp1251")
print(b.decode(encoding="cp1251"), b.decode("cp1251"))
# ('строка', 'строка')


b = bytearray("строка", "cp1251")
print(str(b, "cp1251"))
# 'строка'