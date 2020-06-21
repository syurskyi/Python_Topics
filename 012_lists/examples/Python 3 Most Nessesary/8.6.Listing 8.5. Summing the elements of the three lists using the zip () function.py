# -*- coding: utf-8 -*-

arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30, 40, 50]
arr3 = [100, 200, 300, 400, 500]
arr = [x + y + z for (x, y, z) in zip(arr1, arr2, arr3)]
print(arr)
# Результат выполнения: [111, 222, 333, 444, 555]


print(filter(None, [1, 0, None, [], 2]))
# <filter object at 0x00FD58B0>
print(list(filter(None, [1, 0, None, [], 2])))
# [1, 2]


print([ i for i in [1, 0, None, [], 2] if i ])
# [1, 2]