"""Пример использования функции map"""

string = '2 4 8 15 42'
numbers = map(int, string.split())
print(list(numbers))
