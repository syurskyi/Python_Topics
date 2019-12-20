# -*- coding: utf-8 -*-

"""Операции с множествами (set и frozenset)"""

my_set = {4, 5, 1, 2}

# Количество элементов множества
print('len({}) = {}'.format(my_set, len(my_set)))

print()

# Проверка вхождения элемента
print(4 in my_set)
print(3 not in my_set)
print(9 in my_set)

print()

# Пересекаются ли множества
print({3, 4, 5}.isdisjoint({8, 1, 0}))
print({3, 4, 5}.isdisjoint({1, 2, 3}))

print()

# Проверка включения одного множества в другое
print({1, 7, 9}.issubset({1, 2, 3, 7, 9}))
print({1, 7, 9} <= {1, 2, 3, 7, 9})
print({1, 7, 9, 2, 3} <= {1, 2, 3, 7, 9})

print()

# Проверка строгого включения
print({1, 7, 9} < {1, 2, 3, 7, 9})
print({1, 7, 9, 2, 3} < {1, 2, 3, 7, 9})

print()

# Проверка включения одного множества в другое
print({1, 2, 3, 4}.issuperset({1, 2}))
print({1, 2, 4, 4} >= {1, 2})
print({1, 2, 3, 4} >= {1, 2, 3, 4})

print()

# Проверка строгого включения
print({1, 2, 4, 4} > {1, 2})
print({1, 2, 3, 4} > {1, 2, 3, 4})

print()

# Объединение множеств
print({1, 3}.union({2, 3, 4}))
print({1, 3} | {2, 3, 4})

print()

# Пересечение множеств
print({1, 3}.intersection({2, 3, 4}))
print({1, 3} & {2, 3, 4})

print()

# Разница множеств
print({1, 2, 3, 4}.difference({3, 4, 5}))
print({1, 2, 3, 4} - {3, 4, 5})

print()

# Симметрическая разница
print({1, 2, 3, 4}.symmetric_difference({3, 4, 5, 6}))
print({1, 2, 3, 4} ^ {3, 4, 5, 6})

print()

# Копирование множества
my_set = set('chars')
copy = my_set.copy()
print(copy)
