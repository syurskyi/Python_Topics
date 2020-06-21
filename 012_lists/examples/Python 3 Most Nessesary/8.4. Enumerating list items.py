# -*- coding: utf-8 -*-

arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i, end=" ")

# 1 2 3 4 5


arr = [1, 2, 3, 4]              # Элементы имеют неизменяемый тип (число)
for i in arr:
    i += 10

print(arr)                      # Список не изменился
# [1, 2, 3, 4]
arr = [[1, 2], [3, 4]]          # Элементы имеют изменяемый тип (список)
for i in arr:
    i[0] += 10
print(arr)                      # Список изменился
# [[11, 2], [13, 4]]


arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr[i] *= 2
print(arr)                   # Результат выполнения: [2, 4, 6, 8]


arr = [1, 2, 3, 4]
for i, elem in enumerate(arr):
    arr[i] *= 2
print(arr)                   # Результат выполнения: [2, 4, 6, 8]


arr = [1, 2, 3, 4]
i, c = 0, len(arr)
while i < c:
    arr[i] *= 2
    i += 1
print(arr)                   # Результат выполнения: [2, 4, 6, 8]