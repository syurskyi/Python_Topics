"""Пример использования модуля fractions, который
предоставляет тип данных Fraction -- рациональные числа.
"""

from fractions import Fraction
from decimal import Decimal

# Примеры создания
print(Fraction(16, -10))
print(Fraction(123))
print(Fraction(Decimal('1.1')))
print(Fraction())

print(Fraction('3/7'))
print(Fraction(' -3/7 '))
print(Fraction('1.414213 \t\n'))

print(Fraction('-.125'))
print(Fraction('7e-6'))
print(Fraction(2.25))

print()

obj = Fraction(16, -10)
print('Дробь:', obj)
print('Числитель:', obj.numerator)
print('Знаменатель:', obj.denominator)

print()

# Арифметические операции
print(Fraction(-10, 15) + Fraction(10, 15))
print(Fraction(10, 15) * Fraction(15, 10))
print(Fraction(10, 15) / Fraction(10, 15))
print(Fraction(1, 3) + Fraction(2, 3))
print(Fraction(15, 5) * 12.0)
print(9 ** Fraction(1, 2))
print(Fraction(100, 2) % 12)
print(100 // Fraction(124, 447))
