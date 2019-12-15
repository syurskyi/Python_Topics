d1, d2 = {"a": 1, "b": 2 }, {"a": 3, "c": 4, "d": 5}
print(d1.keys(), d2.keys())                                       # Получаем объект dict_keys
# (dict_keys(['a', 'b']), dict_keys(['a', 'c', 'd']))
print(list(d1.keys()), list(d2.keys()))                           # Получаем список ключей
# (['a', 'b'], ['a', 'c', 'd'])
for k in d1.keys():
  print(k, end=" ")

# a b
print(d1.keys() | d2.keys())                                      # Объединение
# {'a', 'c', 'b', 'd'}
print(d1.keys() - d2.keys())                                      # Разница
# {'b'}
print(d2.keys() - d1.keys())                                      # Разница
# {'c', 'd'}
print(d1.keys() & d2.keys())                                      # Одинаковые ключи
# {'a'}
print(d1.keys() ^ d2.keys())                                      # Уникальные ключи
# {'c', 'b', 'd'}


d = {"a": 1, "b": 2}
print(d.values())                                                 # Получаем объект dict_values
# dict_values([1, 2])
print(list(d.values()))                                           # Получаем список значений
# [1, 2]
print([v for v in d.values()])
# [1, 2]


d = {"a": 1, "b": 2}
print(d.items())                                                  # Получаем объект dict_items
# dict_items([('a', 1), ('b', 2)])
print(list(d.items()))                                            # Получаем список кортежей
# [('a', 1), ('b', 2)]


d = {"a": 1, "b": 2}
print("a" in d)                                                   # Ключ существует
# True
print("c" in d)                                                   # Ключ не существует
# False


d = {"a": 1, "b": 2}
print("c" not in d)                                               # Ключ не существует
# True
print("a" not in d)                                               # Ключ существует
# False


d = {"a": 1, "b": 2}
print(d.get("a"), d.get("c"), d.get("c", 800))
# (1, None, 800)


d = {"a": 1, "b": 2}
print(d.setdefault("a"), d.setdefault("c"), d.setdefault("d", 0))
# (1, None, 0)print()
print(d)
# {'a': 1, 'c': None, 'b': 2, 'd': 0}


d = {"a": 1, "b": 2, "c": 3}
print(d.pop("a"), d.pop("n", 0))
# (1, 0)print(
# d.pop("n") # Ключ отсутствует и нет второго параметра)
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     d.pop("n") # Ключ отсутствует и нет второго параметра
# KeyError: 'n'
print(d)
# {'c': 3, 'b': 2}


d = {"a": 1, "b": 2}
print(d.popitem())                                                # Удаляем произвольный элемент
# ('a', 1)
print(d.popitem())                                                # Удаляем произвольный элемент
# ('b', 2)
# d.popitem() # Словарь пустой. Возбуждается исключение
# Traceback (most recent call last):
#   File "<pyshell#45>", line 1, in <module>
#     d.popitem() # Словарь пустой. Возбуждается исключение
# KeyError: 'popitem(): dictionary is empty'


d = {"a": 1, "b": 2}
d.clear()                                                        # Удаляем все элементы
print(d)                                                         # Словарь теперь пустой
# {}


d = {"a": 1, "b": 2}
d.update(c=3, d=4)
print(d)
# {'a': 1, 'c': 3, 'b': 2, 'd': 4}
d.update({"c": 10, "d": 20})                                     # Словарь
print(d)                                                         # Значения элементов перезаписаны
# {'a': 1, 'c': 10, 'b': 2, 'd': 20}
d.update([("d", 80), ("e", 6)])                                  # Список кортежей
print(d)
# {'a': 1, 'c': 10, 'b': 2, 'e': 6, 'd': 80}
d.update([["a", "str"], ["i", "t"]])                             # Список списков
print(d)
# {'a': 'str', 'c': 10, 'b': 2, 'e': 6, 'd': 80, 'i': 't'}


d1 = {"a": 1, "b": [10, 20]}
d2 = d1.copy()                                                   # Создаем поверхностную копию
print(d1 is d2)                                                  # Это разные объекты
# False
d2["a"] = 800                                                    # Изменяем значение
print(d1, d2)                                                    # Изменилось значение только в d2
# ({'a': 1, 'b': [10, 20]}, {'a': 800, 'b': [10, 20]})
d2["b"][0] = "new"                                               # Изменяем значение вложенного списка
print(d1, d2)                                                    # Изменились значения и в d1, и в d2!!!
# ({'a': 1, 'b': ['new', 20]}, {'a': 800, 'b': ['new', 20]})