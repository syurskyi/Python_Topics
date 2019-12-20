# -*- coding: utf-8 -*-

arr = [1, 2, 3]          # Создаем список
print(arr[0])                   # Получаем элемент по индексу
# 1
arr[0] = 50              # Изменяем элемент по индексу
print(arr)
# [50, 2, 3]

t = (1, 2, 3)            # Создаем кортеж
print(t[0])                     # Получаем элемент по индексу
# 1
# t[0] = 50                # Изменить элемент по индексу нельзя!
# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     t[0] = 50                # Изменить элемент по индексу нельзя!
# TypeError: 'tuple' object does not support item assignment


print(set([0, 1, 1, 2, 3, 3, 4]))
# {0, 1, 2, 3, 4}


r = range(0, 101, 10)
for i in r:
  print(i, end = " ")

# 0 10 20 30 40 50 60 70 80 90 100

print(list())                   # Создаем пустой список
# []
print(list("String"))           # Преобразуем строку в список
# ['S', 't', 'r', 'i', 'n', 'g']
print(list((1, 2, 3, 4, 5)))    # Преобразуем кортеж в список
# [1, 2, 3, 4, 5]


arr = [1, "str", 3, "4"]
print(arr)
# [1, 'str', 3, '4']


arr = []           # Создаем пустой список
arr.append(1)      # Добавляем элемент1 (индекс 0)
arr.append("str")  # Добавляем элемент2 (индекс 1)
print(arr)
# [1, 'str']


arr = []
# arr[] = 10
# SyntaxError: invalid syntax
# arr[0] = 10
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     arr[0] = 10
# IndexError: list assignment index out of range


x = y = [1, 2]       # Якобы создали два объекта
print(x, y)
# ([1, 2], [1, 2])


y[1] = 100           # Изменяем второй элемент
print(x, y)                 # Изменилось значение сразу в двух переменных
# ([1, 100], [1, 100])


x, y = [1, 2], [1, 2]
y[1] = 100           # Изменяем второй элемент
print(x, y)
# ([1, 2], [1, 100])


arr = [[]] * 2         # Якобы создали два вложенных списка
print(arr)
# [[], []]
arr[0].append(5)            # Добавляем элемент
print(arr)                  # Изменились два элемента
# [[5], [5]]


arr = []
for i in range(2):
  arr.append([])

print(arr)
# [[], []]
arr[0].append(5); print(arr)
# [[5], []]


arr = [ [] for i in range(2) ]
print(arr)
# [[], []]
arr[0].append(5); print(arr)
# [[5], []]


x = y = [1, 2]        # Неправильно
print(x is y)                 # Переменные содержат ссылку на один и тот же список
# True
x, y = [1, 2], [1, 2] # Правильно
print(x is y)              # Это разные объекты
# False