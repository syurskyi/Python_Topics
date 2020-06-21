# -*- coding: utf-8 -*-

"""Операции с изменяемыми множествами (set)"""

my_set = {1, 3, 5}

my_set.update({2, 3, 4})  # my_set |= {2, 3, 4}
print(my_set)

my_set.intersection_update({0, 1, 2, 3, 10})  # my_set &= {0, 1, 2, 3, 10}
print(my_set)

my_set.difference_update({1})  # my_set -= {1}
print(my_set)

my_set.symmetric_difference_update({3, 4})  # my_set ^= {3, 4}
print(my_set)

my_set.add(5)  # my_set |= {5}
print(my_set)

my_set.remove(2)  # my_set -= {2}, но выбрасывает KeyError, если такого элемента нет
print(my_set)

my_set.discard(2)  # my_set -= {2}
print(my_set)

print(my_set.pop())
print(my_set)

my_set.clear()
print(my_set)
