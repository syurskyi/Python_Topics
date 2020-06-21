# -*- coding: utf-8 -*-

arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr[i] *= 2
print(arr)                   # Результат выполнения: [2, 4, 6, 8]


arr = [1, 2, 3, 4]
arr = [ i * 2 for i in arr ]
print(arr)                   # Результат выполнения: [2, 4, 6, 8]


arr = [1, 2, 3, 4]
arr = [ i * 10 for i in arr if i % 2 == 0 ]
print(arr)                   # Результат выполнения: [20, 40]


arr = []
for i in [1, 2, 3, 4]:
    if i % 2 == 0:           # Если число четное
        arr.append(i * 10)   # Добавляем элемент
print(arr)                   # Результат выполнения: [20, 40]


arr = [[1, 2], [3, 4], [5, 6]]
arr = [ j * 10 for i in arr for j in i if j % 2 == 0 ]
print(arr)                   # Результат выполнения: [20, 40, 60]


arr = []
for i in [[1, 2], [3, 4], [5, 6]]:
    for j in i:
        if j % 2 == 0:          # Если число четное
            arr.append(j * 10)  # Добавляем элемент
print(arr)                      # Результат выполнения: [20, 40, 60]


arr = [1, 4, 12, 45, 10]
print(sum((i for i in arr if i % 2 == 0)))
#
