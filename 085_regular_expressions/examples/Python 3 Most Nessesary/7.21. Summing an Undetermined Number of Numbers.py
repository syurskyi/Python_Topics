# -*- coding: utf-8 -*-

import re
print("Введите слово 'stop' для получения результата")
summa = 0
p = re.compile(r"^[-]?[0-9]+$", re.S)
while True:
    x = input("Введите число: ")
    if x == "stop":
        break    # Выход из цикла
    if not p.search(x):
        print("Необходимо ввести число, а не строку!")
        continue # Переходим на следующую итерацию цикла
    x = int(x)   # Преобразуем строку в число
    summa += x
print("Сумма чисел равна:", summa)
input()


p = re.compile(r"(?P<num>[0-9]+)(?P<str>[a-z]+)")
m = p.search("123456string 67890text")
m
# <_sre.SRE_Match object at 0x00FC9DE8>
m.re.groups, m.re.groupindex
# (2, {'num': 1, 'str': 2})
p.groups, p.groupindex
# (2, {'num': 1, 'str': 2})
m.string
# '123456string 67890text'
m.lastindex, m.lastgroup
# (2, 'str')
m.pos, m.endpos
# (0, 22)


p = re.compile(r"(?P<num>[0-9]+)(?P<str>[a-z]+)")
m = p.search("123456string 67890text")
m.group(), m.group(0) # Полное соответствие шаблону
# ('123456string', '123456string')
m.group(1), m.group(2)         # Обращение по индексу
# ('123456', 'string')
m.group("num"), m.group("str") # Обращение по названию
# ('123456', 'string')
m.group(1, 2), m.group("num", "str") # Несколько параметров
# (('123456', 'string'), ('123456', 'string'))


p = re.compile(r"(?P<num>[0-9]+)(?P<str>[a-z])?")
m = p.search("123456")
m.groupdict()
# {'num': '123456', 'str': None}
m.groupdict("")
# {'num': '123456', 'str': ''}


p = re.compile(r"(?P<num>[0-9]+)(?P<str>[a-z])?")
m = p.search("123456")
m.groups()
# ('123456', None)
m.groups("")
# ('123456', '')


p = re.compile(r"(?P<num>[0-9]+)(?P<str>[a-z]+)")
s = "str123456str"
m = p.search(s)
m.start(), m.end(), m.span()
# (3, 12, (3, 12))
m.start(1), m.end(1), m.start("num"), m.end("num")
# (3, 9, 3, 9)
m.start(2), m.end(2), m.start("str"), m.end("str")
# (9, 12, 9, 12)
m.span(1), m.span("num"), m.span(2), m.span("str")
# ((3, 9), (3, 9), (9, 12), (9, 12))
s[m.start(1):m.end(1)], s[m.start(2):m.end(2)]
# ('123456', 'str')


p = re.compile(r"<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>")
m = p.search("<br><hr>")
m.expand(r"<\2><\1>")             # \номер
# '<hr><br>'
m.expand(r"<\g<2>><\g<1>>")       # \g<номер>
# '<hr><br>'
m.expand(r"<\g<tag2>><\g<tag1>>") # \g<название>
# '<hr><br>'