# -*- coding: utf-8 -*-

import re
p = re.compile(r"[0-9]+")
print("Найдено" if p.match("str123") else "Нет")
# Нет
print("Найдено" if p.match("str123", 3) else "Нет")
# Найдено
print("Найдено" if p.match("123str") else "Нет")
# Найдено


p = r"[0-9]+"
print("Найдено" if re.match(p, "str123") else "Нет")
# Нет
print("Найдено" if re.match(p, "123str") else "Нет")
# Найдено
p = re.compile(r"[0-9]+")
print("Найдено" if re.match(p, "123str") else "Нет")
# Найдено


p = re.compile(r"[0-9]+")
print("Найдено" if p.search("str123") else "Нет")
# Найдено
print("Найдено" if p.search("123str") else "Нет")
# Найдено
print("Найдено" if p.search("123str", 3) else "Нет")
# Нет


p = r"[0-9]+"
print("Найдено" if re.search(p, "str123") else "Нет")
# Найдено
p = re.compile(r"[0-9]+")
print("Найдено" if re.search(p, "str123") else "Нет")
# Найдено


p = re.compile("[Pp]ython")
print("Найдено" if p.fullmatch("Python") else "Нет")
# Найдено
print("Найдено" if p.fullmatch("py") else "Нет")
# Нет
print("Найдено" if p.fullmatch("PythonWare") else "Нет")
# Нет
print("Найдено" if p.fullmatch("PythonWare", 0, 6) else "Нет")
# Найдено


p = "[Pp]ython"
print("Найдено" if re.fullmatch(p, "Python") else "Нет")
# Найдено
print("Найдено" if re.fullmatch(p, "py") else "Нет")
# Нет