def func(x, y):
    for i in range(1, x+1):
       yield i ** y

i = func(3, 3)
print(i.__next__())      # Выведет: 1 (1 ** 3)
print(i.__next__())      # Выведет: 8 (2 ** 3)
print(i.__next__())      # Выведет: 27 (3 ** 3)
print(i.__next__())      # Исключение StopIteration
