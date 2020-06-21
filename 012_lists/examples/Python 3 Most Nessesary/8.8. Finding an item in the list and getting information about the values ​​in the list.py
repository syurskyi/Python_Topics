# -*- coding: utf-8 -*-

print(2 in [1, 2, 3, 4, 5], 6 in [1, 2, 3, 4, 5])             # Проверка на вхождение
# (True, False)
print(2 not in [1, 2, 3, 4, 5], 6 not in [1, 2, 3, 4, 5])     # Проверка на невхождение
# (False, True)


arr = [1, 2, 1, 2, 1]
print(arr.index(1), arr.index(2))
# (0, 1)
print(arr.index(1, 1), arr.index(1, 3, 5))
# (2, 4)
# print(arr.index(3))
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     arr.index(3)
# ValueError: 3 is not in list


arr = [1, 2, 1, 2, 1]
print(arr.count(1), arr.count(2))
# (3, 2)
print(arr.count(3))                  # Элемент не входит в список
# 0


arr = [1, 2, 3, 4, 5]
print(max(arr), min(arr))
(5, 1)


print(any([0, None]), any([0, None, 1]), any([]))
# (False, True, False)


print(all([0, None]), all([0, None, 1]), all([]), all(["str", 10]))
# (False, False, True, True)