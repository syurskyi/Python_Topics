# -*- coding: utf-8 -*-

arr = {"x": 1, "y": 2, "z": 3}
arr.keys()
# dict_keys(['y', 'x', 'z'])
for key in arr.keys():     # Использование метода keys()
    print(key, arr[key])


for key in arr:            # Словари также поддерживают итерации
    print(key, arr[key])


arr = {"x": 1, "y": 2, "z": 3}
for key in sorted(arr):
        print(key, arr[key])
