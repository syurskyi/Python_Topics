# -*- coding: utf-8 -*-

s = "Python"
print(s[0], s[1], s[2], s[3], s[4], s[5])
# ('P', 'y', 't', 'h', 'o', 'n')


s = "Python"
# s[10]
"""
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s[10]
IndexError: string index out of range
"""


s = "Python"
print(s[-1], s[len(s)-1])
# ('n', 'n')


s = "Python"
# s[0] = "J"                          # Изменить строку нельзя
"""
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s[0] = "J"                          # Изменить строку нельзя
TypeError: 'str' object does not support item assignment
"""

s = "Python"


print(s[:]) # Возвращается фрагмент от позиции 0 до конца строки
# 'Python'


print(s[::-1]) # Указываем отрицательное значение в параметре <Шаг>
# 'nohtyP'


print("J" + s[1:]) # Извлекаем фрагмент от символа 1 до конца строки
# 'Jython'


print(s[:-1]) # Возвращается фрагмент от 0 до len(s)-1
# 'Pytho'


print(s[0:1]) # Символ с индексом 1 не входит в диапазон
# 'P'

print(s[-1:]) # Получаем фрагмент от len(s)-1 до конца строки
# 'n'


print(s[2:5]) # Возвращаются символы с индексами 2, 3 и 4
# 'tho'


print(len("Python"), len("\r\n\t"), len(r"\r\n\t"))
# (6, 3, 6)


s = "Python"
for i in range(len(s)): print(s[i], end=" ")


s = "Python"
for i in s: print(i, end=" ")


print("Строка1" + "Строка2")
# Строка1Строка2


print("Строка1" "Строка2")
# Строка1Строка2


s = "Строка1", "Строка2"
print(type(s))                        # Получаем кортеж, а не строку
# <class 'tuple'>


s = "Строка1"
print(s + "Строка2")           # Нормально
# Строка1Строка2
# print(s "Строка2")             # Ошибка
# SyntaxError: invalid syntax


print("string" + str(10))
# 'string10'


print("-" * 20)
'--------------------'
print("yt" in "Python")               # Найдено
# True
print("yt" in "Perl")                 # Не найдено
# False
print("PHP" not in "Python")          # Не найдено
# True