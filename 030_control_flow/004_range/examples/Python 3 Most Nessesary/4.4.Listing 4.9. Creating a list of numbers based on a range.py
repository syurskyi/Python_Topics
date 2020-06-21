# -*- coding: utf-8 -*-

obj = range(len([1, 2, 3]))
print(obj)
print(range(0, 3))
print(obj[0], obj[1], obj[2])      # Доступ по индексу
# (0, 1, 2)
obj[0:2]                    # Получение среза
print(range(0, 2))
i = iter(obj)
print(next(i), next(i), next(i))   # Доступ с помощью итераторов
# (0, 1, 2)
print(list(obj))                   # Преобразование диапазона в список
# [0, 1, 2]
print(1 in obj, 7 in obj)          # Проверка вхождения значения
# (True, False)

obj = range(1, 5)
print(obj.index(1), obj.index(4))
# (0, 3)
# obj.index(5)
# ... Фрагмент опущен ...
# ValueError: 5 is not in range

obj = range(1, 5)
print(obj.count(1), obj.count(10))
# (1, 0)
