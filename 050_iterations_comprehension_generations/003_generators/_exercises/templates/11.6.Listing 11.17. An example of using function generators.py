def func(x, y):
    for i in range(1, x+1):
        yield i ** y
for n in func(10, 2):
    print(n, end=" ")    # Выведет: 1 4 9 16 25 36 49 64 81 100
print()                  # Вставляем пустую строку
for n in func(10, 3):
    print(n, end=" ")    # Выведет: 1 8 27 64 125 216 343 512 729 1000
