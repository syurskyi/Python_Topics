# An example of using function generators

def func(x, y):
    for i in range(1, x+1):
        yield i ** y
for n in func(10, 2):
    print(n, end=" ")    # Выведет: 1 4 9 16 25 36 49 64 81 100
print()                  # Вставляем пустую строку
for n in func(10, 3):
    print(n, end=" ")    # Выведет: 1 8 27 64 125 216 343 512 729 1000

print()
# ######################################################################################################################
#  Using the __next __ () parameter

def func(x, y):
    for i in range(1, x + 1):
        yield i ** y

i = func(3, 3)
print(i.__next__())  # Выведет: 1 (1 ** 3)
print(i.__next__())  # Выведет: 8 (2 ** 3)
print(i.__next__())  # Выведет: 27 (3 ** 3)
# print(i.__next__())  # Исключение StopIteration

print()
# ######################################################################################################################
#  Calling one generator function fro… (simple case)

def gen(l):
    for e in l:
        yield from range(1, e + 1)

l = [5, 10]
for i in gen([5, 10]): print(i, end=" ")

print()
# ######################################################################################################################
# Calling one function generator fro…er (hard case)

def gen2(n):
    for e in range(1, n + 1):
        yield  e * 2

def gen(l):
    for e in l:
        yield  from gen2(e)

l = [5, 10]
for i in gen([5, 10]): print(i, end=" ")

print()