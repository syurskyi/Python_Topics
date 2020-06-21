# -*- coding: utf-8 -*-

print("""Какой операционной системой вы пользуетесь?
1 — Windows 8
2 — Windows 7
3 — Windows Vista
4 — Windows XP
5 — Другая""")
os = input("Введите число, соответствующее ответу: ")
if os != "":
    if   os == "1":
        print("Вы выбрали: Windows 8")
    elif os == "2":
        print("Вы выбрали: Windows 7")
    elif os == "3":
        print("Вы выбрали: Windows Vista")
    elif os == "4":
        print("Вы выбрали: Windows XP")
    elif os == "5":
        print("Вы выбрали: другая")
    else:
        print("Мы не смогли определить вашу операционную систему")
else:
    print("Вы не ввели число")
input()


print("Yes" if 10 % 2 == 0 else "No")
# Yes
s = "Yes" if 10 % 2 == 0 else "No"
s
# 'Yes'
s = "Yes" if 11 % 2 == 0 else "No"
s
# 'No'