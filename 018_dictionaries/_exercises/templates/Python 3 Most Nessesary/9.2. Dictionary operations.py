# # -*- coding: utf-8 -*-
#
# d = {1: "int", "a": "str", (1, 2): "tuple"}
# print(d[1], d["a"], d[(1, 2)])
# # ('int', 'str', 'tuple')
#
#
# d = {"a": 1, "b": 2}
# # d["c"]             # Обращение к несуществующему элементу
# # Traceback (most recent call last):
# #   File "<pyshell#49>", line 1, in <module>
# #     d["c"]             # Обращение к несуществующему элементу
# # KeyError: 'c'
#
#
# d = {"a": 1, "b": 2}
# print("a" in d)           # Ключ существует
# # True
# print("c" in d)           # Ключ не существует
# # False
#
#
# d = {"a": 1, "b": 2}
# print("c" not in d)           # Ключ не существует
# # True
# print("a" not in d)           # Ключ существует
# # False
#
#
# d = {"a": 1, "b": 2}
# print ?.g. a ?.g.. c ?.g.. c 800
# # (1, None, 800)
#
#
# d = {"a": 1, "b": 2}
# print ?.s_d_ a ?.s_d_ c ?.s_d_ d, 0
# # (1, None, 0)
# print(d)
# # {'a': 1, 'c': None, 'b': 2, 'd': 0}
#
# d = {"a": 1, "b": 2}
# d["a"] = 800               # Изменение элемента по ключу
# d["c"] = "string"          # Будет добавлен новый элемент
# print(d)
# # {'a': 800, 'c': 'string', 'b': 2}
#
#
# d = {"a": 1, "b": 2}
# print(len(d))          # Получаем количество ключей в словаре
# # 2
#
#
# d = {"a": 1, "b": 2}
# del d["b"]; print(d)   # Удаляем элемент с ключом "b" и выводим словарь
# # {'a': 1}