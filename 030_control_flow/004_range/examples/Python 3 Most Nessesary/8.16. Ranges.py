# -*- coding: utf-8 -*-

arr = [1, 2, 3, 4, 5, 6]
for i, elem in enumerate(arr):
    if elem % 2 == 0:
        arr[i] *= 2
print(arr)                # Результат выполнения: [1, 4, 3, 8, 5, 12]

arr = [1, 2]
obj = enumerate(arr, start=2)
print(next(obj))
# (2, 1)
print(next(obj))
# (3, 2)
# next(obj)
# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     next(obj)
# StopIteration


r = range(1, 10)
for i in r:
    print(i, end = " ")
# 1 2 3 4 5 6 7 8 9
r = range(10, 110, 10)
for i in r:
    print(i, end = " ")
# 10 20 30 40 50 60 70 80 90 100
r = range(10, 1, -1)
for i in r:
    print(i, end = " ")
# 10 9 8 7 6 5 4 3 2


print(list(range(1, 10)))           # Преобразуем в список
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(range(1, 10)))           # Преобразуем в кортеж
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(set(range(1, 10)))            # Преобразуем в множество
# {1, 2, 3, 4, 5, 6, 7, 8, 9}


r = range(1, 10)
print(r[2], r[-1])
# (3, 9)
print(r[2:4])
# range(3, 5)
print(2 in r, 12 in r)
# (True, False)
print(3 not in r, 13 not in r)
# (False, True)
print(len(r), min(r), max(r))
# (9, 1, 9)
print(r.index(4), r.count(4))
# (3, 1)

print(range(1, 10) == range(1, 10, 1))
# True
print(range(1, 10, 2) == range(1, 11, 2))
# True
print(range(1, 10, 2) == range(1, 12, 2))
# False


print(range(1, 10, 2) != range(1, 12, 2))
# True
print(range(1, 10) != range(1, 10, 1))
# False

r = range(1, 10)
print(r.start, r.stop, r.step)
(1, 10, 1)