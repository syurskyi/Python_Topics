# Переменные, объединённые в кортеж, могут стоять в левой части
# присваивания или заголовке цикла for. Тогда им присваиваются
# соответствующие значения итерабельного объекта.

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

print()

# В список rest будут помещены оставшиеся элементы последовательности
a, b, *rest = range(10)
print(a)
print(b)
print(rest)

print()

# Поменять местами значения двух переменных
print(a, b)
a, b = b, a
print(a, b)

print()

# Список кортежей
tuples = [(x, y) for x in range(3) for y in range(3)]
# Итерирование списка
for t in tuples:
    print(t)
# Итерирование с распаковкой
for x, y in tuples:
    print(x, y)
