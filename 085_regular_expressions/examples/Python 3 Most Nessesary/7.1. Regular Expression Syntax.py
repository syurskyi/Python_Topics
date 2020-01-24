# -*- coding: utf-8 -*-

import re
p = re.compile(r"^[а-яе]+$", re.I | re.U)
print("Найдено" if p.search("АБВГДЕЕ") else "Нет")
# Найдено
p = re.compile(r"^[а-яе]+$", re.U)
print("Найдено" if p.search("АБВГДЕЕ") else "Нет")
# Нет


p = re.compile(r"^.$")
print("Найдено" if p.search("\n") else "Нет")
# Нет
p = re.compile(r"^.$", re.M)
print("Найдено" if p.search("\n") else "Нет")
# Нет
p = re.compile(r"^.$", re.S)
print("Найдено" if p.search("\n") else "Нет")
# Найдено


p = re.compile(r"""^ # Привязка к началу строки
              [0-9]+ # Строка должна содержать одну цифру (или более)
              $      # Привязка к концу строки
        """, re.X | re.S)
print("Найдено" if p.search("1234567890") else "Нет")
# Найдено
print("Найдено" if p.search("abcd123") else "Нет")
# Нет

p = re.compile(r"^\w+$")

p = re.compile("^\\w+$")