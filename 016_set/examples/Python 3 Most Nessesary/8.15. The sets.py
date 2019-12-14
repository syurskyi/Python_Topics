s = set()
print(s)
# set([])


print(set("string"))                   # Преобразуем строку
# set(['g', 'i', 'n', 's', 'r', 't'])
print(set([1, 2, 3, 4, 5]))            # Преобразуем список
# set([1, 2, 3, 4, 5])
print(set((1, 2, 3, 4, 5)))           # Преобразуем кортеж
# set([1, 2, 3, 4, 5])
print(set([1, 2, 3, 1, 2, 3]))  # Остаются только уникальные элементы
# set([1, 2, 3])


for i in set([1, 2, 3]):
  print(i)
# 1 2 3


print(len(set([1, 2, 3])))
# 3


s = set([1, 2, 3])
print(s.union(set([4, 5, 6])), s | set([4, 5, 6]))
# (set([1, 2, 3, 4, 5, 6]), set([1, 2, 3, 4, 5, 6]))


print(set([1, 2, 3]) | set([1, 2, 3]))
# set([1, 2, 3])


s = set([1, 2, 3])
s.update(set([4, 5, 6]))
print(s)
# set([1, 2, 3, 4, 5, 6])
s |= set([7, 8, 9])
print(s)
# set([1, 2, 3, 4, 5, 6, 7, 8, 9])


print(set([1, 2, 3]) - set([1, 2, 4]))
# set([3])
s = set([1, 2, 3])
print(s.difference(set([1, 2, 4])))
# set([3])


s = set([1, 2, 3])
s.difference_update(set([1, 2, 4]))
print(s)
# set([3])
s -= set([3, 4, 5])
print(s)
# set([])


print(set([1, 2, 3]) & set([1, 2, 4]))
# set([1, 2])
s = set([1, 2, 3])
print(s.intersection(set([1, 2, 4])))
# set([1, 2])


s = set([1, 2, 3])
s.intersection_update(set([1, 2, 4]))
print(s)
# set([1, 2])
s &= set([1, 6, 7])
print(s)
# set([1])


s = set([1, 2, 3])
print(s ^ set([1, 2, 4]), s.symmetric_difference(set([1, 2, 4])))
# (set([3, 4]), set([3, 4]))
print(s ^ set([1, 2, 3]), s.symmetric_difference(set([1, 2, 3])))
# (set([]), set([]))
print(s ^ set([4, 5, 6]), s.symmetric_difference(set([4, 5, 6])))
# (set([1, 2, 3, 4, 5, 6]), set([1, 2, 3, 4, 5, 6]))


s = set([1, 2, 3])
s.symmetric_difference_update(set([1, 2, 4]))
print(s)
# set([3, 4])
s ^= set([3, 5, 6])
print(s)
# set([4, 5, 6])


s = set([1, 2, 3, 4, 5])
print(1 in s, 12 in s)
# (True, False)


s = set([1, 2, 3, 4, 5])
print(1 in s, 12 in s)
# (False, True)


print(set([1, 2, 3]) == set([1, 2, 3]))
# True
print(set([1, 2, 3]) == set([3, 2, 1]))
# True
print(set([1, 2, 3]) == set([1, 2, 3, 4]))
# False


s = set([1, 2, 3])
print(s <= set([1, 2]), s <= set([1, 2, 3, 4]))
# (False, True)
print(s.issubset(set([1, 2])), s.issubset(set([1, 2, 3, 4])))
# (False, True)


s = set([1, 2, 3])
print(s < set([1, 2, 3]), s < set([1, 2, 3, 4]))
# (False, True)


s = set([1, 2, 3])
print(s >= set([1, 2]), s >= set([1, 2, 3, 4]))
# (True, False)
print(s.issuperset(set([1, 2])), s.issuperset(set([1, 2, 3, 4])))
# (True, False)


s = set([1, 2, 3])
print(s > set([1, 2]), s > set([1, 2, 3]))
# (True, False)


s = set([1, 2, 3])
print(s.isdisjoint(set([4, 5, 6])))
# True
print(s.isdisjoint(set([1, 3, 5])))
# False


s = set([1, 2, 3])
c = s; print(s is c) # С помощью = копию создать нельзя!
# True
c = s.copy()  # Создаем копию объекта
print(c)
set([1, 2, 3])
print(s is c)        # Теперь это разные объекты
# False


s = set([1, 2, 3])
s.add(4); print(s)
# set([1, 2, 3, 4])

s = set([1, 2, 3])
s.remove(3); print(s)        # Элемент существует
# set([1, 2])
# s.remove(5)           # Элемент НЕ существует
# Traceback (most recent call last):
#   File "<pyshell#78>", line 1, in <module>
#     s.remove(5)           # Элемент НЕ существует
# KeyError: 5


s = set([1, 2, 3])
s.discard(3); print(s)       # Элемент существует
# set([1, 2])
s.discard(5); print(s)       # Элемент НЕ существует
# set([1, 2])


s = set([1, 2])
s.pop(), print(s)
# (1, set([2]))
s.pop(), print(s)
# (2, set([]))
# s.pop() # Если нет элементов, то будет ошибка
# Traceback (most recent call last):
#   File "<pyshell#89>", line 1, in <module>
#     s.pop() # Если нет элементов, то будет ошибка
# KeyError: 'pop from an empty set'
#

s = set([1, 2, 3])
s.clear(); print(s)
# set([])


print({x for x in [1, 2, 1, 2, 1, 2, 3]})
# {1, 2, 3}


print({x for x in [1, 2, 1, 2, 1, 2, 3] if x % 2 == 0})
# {2}


f = frozenset()
print(f)
# frozenset([])


print(frozenset("string"))                    # Преобразуем строку
# frozenset(['g', 'i', 'n', 's', 'r', 't'])
print(frozenset([1, 2, 3, 4, 4]))            # Преобразуем список
# frozenset([1, 2, 3, 4])
print(frozenset((1, 2, 3, 4, 4)))             # Преобразуем кортеж
# frozenset([1, 2, 3, 4])