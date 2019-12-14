# -*- coding: utf-8 -*-

s = "пример пример Пример"
print(s.find("при"), s.find("При"), s.find("тест"))
# (0, 14, -1)
print(s.find("при", 9), s.find("при", 0, 6), s.find("при", 7, 12))
# (-1, 0, 7)


s = "пример пример Пример"
print(s.index("при"), s.index("при", 7, 12), s.index("При", 1))
# (0, 7, 14)
# print(s.index("тест"))
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     s.index("тест")
# ValueError: substring not found


s = "пример пример Пример Пример"
print(s.rfind("при"), s.rfind("При"), s.rfind("тест"))
# (7, 21, -1)
print(s.find("при", 0, 6), s.find("При", 10, 20))
# (0, 14)


s = "пример пример Пример Пример"
print(s.rindex("при"), s.rindex("При"), s.rindex("при", 0, 6))
# (7, 21, 0)
# print(s.rindex("тест"))
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     s.rindex("тест")
# ValueError: substring not found


s = "пример пример Пример Пример"
print(s.count("при"), s.count("при", 6), s.count("При"))
# (2, 1, 2)
print(s.count("тест"))
0


s = "пример пример Пример Пример"
print(s.startswith("при"), s.startswith("При"))
# (True, False)
print(s.startswith("при", 6), s.startswith("При", 14))
# (False, True)


s = "пример пример Пример Пример"
print(s.startswith(("при", "При")))
# True


s = "подстрока ПОДСТРОКА"
print(s.endswith("ока"), s.endswith("ОКА"))
# (False, True)
print(s.endswith("ока", 0, 9))
# True


s = "подстрока ПОДСТРОКА"
print(s.endswith(("ока", "ОКА")))
# True

s = "Привет, Петя"
print(s.replace("Петя", "Вася"))
# Привет, Вася
print(s.replace("петя", "вася")) # Зависит от регистра
# Привет, Петя
s = "strstrstrstrstr"
print(s.replace("str", ""), s.replace("str", "", 3))
# ('', 'strstr')


s = "Пример"
d = {ord("П"): None, ord("р"): ord("Р")}
print(d)
# {1088: 1056, 1055: None}
print(s.translate(d))
# 'РимеР'


t = str.maketrans({"а": "А", "о": "О", "с": None})
print(t)
# {1072: 'А', 1089: None, 1086: 'О'}
print("строка".translate(t))
# 'трОкА'


t = str.maketrans("абвгдежзи", "АБВГДЕЖЗИ")
print(t)
# {1072: 1040, 1073: 1041, 1074: 1042, 1075: 1043, 1076: 1044,
# 1077: 1045, 1078: 1046, 1079: 1047, 1080: 1048}
print("абвгдежзи".translate(t))
# 'АБВГДЕЖЗИ'


t = str.maketrans("123456789", "0" * 9, "str")
print(t)
# {116: None, 115: None, 114: None, 49: 48, 50: 48, 51: 48,
# 52: 48, 53: 48, 54: 48, 55: 48, 56: 48, 57: 48}
print("str123456789str".translate(t))
# '000000000'