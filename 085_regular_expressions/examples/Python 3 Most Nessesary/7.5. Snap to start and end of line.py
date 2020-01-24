# -*- coding: utf-8 -*-

import re                     # Подключаем модуль
p = re.compile(r"[0-9]+$", re.S)
if p.search("Строка245"):
    print("Есть число в конце строки")
else:
    print("Нет числа в конце строки")
# Выведет: Есть число в конце строки
p = re.compile(r"^[0-9]+", re.S)
if p.search("Строка245"):
    print("Есть число в начале строки")
else:
    print("Нет числа в начале строки")
# Выведет: Нет числа в начале строки
input()


p = re.compile(r"\bpython\b")
print("Найдено" if p.search("python") else "Нет")
# Найдено
print("Найдено" if p.search("pythonware") else "Нет")
# Нет
p = re.compile(r"\Bth\B")
print("Найдено" if p.search("python") else "Нет")
# Найдено
print("Найдено" if p.search("this") else "Нет")
# Нет


p = re.compile(r"красн((ая)|(ое))")
print("Найдено" if p.search("красная") else "Нет")
# Найдено
print("Найдено" if p.search("красное") else "Нет")
# Найдено
print("Найдено" if p.search("красный") else "Нет")
# Нет


s = "<b>Text1</b>Text2<b>Text3</b>"
p = re.compile(r"<b>.*</b>", re.S)
p.findall(s)
# ['<b>Text1</b>Text2<b>Text3</b>']