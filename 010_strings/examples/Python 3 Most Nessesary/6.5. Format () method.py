# -*- coding: utf-8 -*-

print("Символы {{ и }} — {0}".format("специальные"))
# Символы { и } — специальные


print("{0} — {1} — {2}".format(10, 12.3, "string"))      # Индексы
# '10 — 12.3 — string'
arr = [10, 12.3, "string"]
print("{0} — {1} — {2}".format(*arr))                    # Индексы
# '10 — 12.3 — string'
print("{model} — {color}".format(color="red", model="BMW")) # Ключи
# 'BMW — red'
d = {"color": "red", "model": "BMW"}
print("{model} — {color}".format(**d))                   # Ключи
# 'BMW — red'
print("{color} — {0}".format(2015, color="red"))         # Комбинация
# 'red — 2015'


arr = [10, [12.3, "string"]]
print("{0[0]} — {0[1][0]} — {0[1][1]}".format(arr))      # Индексы
# '10 — 12.3 — string'
print("{arr[0]} — {arr[1][1]}".format(arr=arr))        # Индексы
'10 — string'


class Car:
    color, model = "red", "BMW"


car = Car()
print("{0.model} — {0.color}".format(car))              # Атрибуты
# 'BMW — red'


print("{} — {} — {} — {n}".format(1, 2, 3, n=4))  # "{0} — {1} — {2} — {n}"
# '1 — 2 — 3 — 4'
print("{} — {} — {n} — {}".format(1, 2, 3, n=4))  # "{0} — {1} — {n} — {2}"
# '1 — 2 — 4 — 3'


print("{0!s}".format("строка"))                   # str()
# строка
print("{0!r}".format("строка"))                   # repr()
# 'строка'
print("{0!a}".format("строка"))                   # ascii()
# '\u0441\u0442\u0440\u043e\u043a\u0430'

print("'{0:10}' '{1:3}'".format(3, "string"))
# "'         3' 'string'"

print("'{0:{1}}'".format(3, 10)) # 10 — это ширина поля
# "'         3'"

print("'{0:<10}' '{1:>10}' '{2:^10}'".format(3, 3, 3))
# "'3         ' '         3' '    3     '"


print("'{0:=10}' '{1:=10}'".format(-3, 3))
# "'-        3' '         3'"


print("'{0:=010}' '{1:=010}'".format(-3, 3))
# "'-000000003' '0000000003'"


print("'{0:0=10}' '{1:0=10}'".format(-3, 3))
# "'-000000003' '0000000003'"
print("'{0:*<10}' '{1:+>10}' '{2:.^10}'".format(3, 3, 3))
# "'3*********' '+++++++++3' '....3.....'"


print("'{0:+}' '{1:+}' '{0:-}' '{1:-}'".format(3, -3))
# "'+3' '-3' '3' '-3'"
print("'{0: }' '{1: }'".format(3, -3))       # Пробел
# "' 3' '-3'"

print("'{0:b}' '{0:#b}'".format(3))
# "'11' '0b11'"

print("'{0:c}'".format(100))
# "'d'"

import locale
print(locale.setlocale(locale.LC_NUMERIC, 'Russian_Russia.1251'))
# 'Russian_Russia.1251'
print("{0:n}".format(100000000).replace("\uffa0", " "))
# 100 000 000

import locale
print(locale.setlocale(locale.LC_NUMERIC, "Russian_Russia.1251"))
# 'Russian_Russia.1251'
print(print(locale.format("%d", 100000000, grouping = True)))
# 100 000 000
print(locale.localeconv()["thousands_sep"])
# '\xa0'

print(print("{0:,d}".format(100000000)))
# 100,000,000

print("'{0:d}' '{0:o}' '{0:#o}'".format(511))
# "'511' '777' '0o777'"

print("'{0:x}' '{0:#x}'".format(255))
# "'ff' '0xff'"

print("'{0:X}' '{0:#X}'".format(255))
# "'FF' '0XFF'"

print("'{0:f}' '{1:f}' '{2:f}'".format(30, 18.6578145, -2.5))
# "'30.000000' '18.657815' '-2.500000'"

print("'{0:.7f}' '{1:.2f}'".format(18.6578145, -2.5))
# "'18.6578145' '-2.50'"

print("'{0:e}' '{1:e}'".format(3000, 18657.81452))
# "'3.000000e+03' '1.865781e+04'"

print("'{0:E}' '{1:E}'".format(3000, 18657.81452))
# "'3.000000E+03' '1.865781E+04'"

print("'{0:.2e}' '{1:.2E}'".format(3000, 18657.81452))
# "'3.00e+03' '1.87E+04'"

print("'{0:g}' '{1:g}'".format(0.086578, 0.000086578))
# "'0.086578' '8.6578e-05'"

print("'{0:G}' '{1:G}'".format(0.086578, 0.000086578))
# "'0.086578' '8.6578E-05'"

print("'{0:%}' '{1:.4%}'".format(0.086578, 0.000086578))
# "'8.657800%' '0.0087%'"
