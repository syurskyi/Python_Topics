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
