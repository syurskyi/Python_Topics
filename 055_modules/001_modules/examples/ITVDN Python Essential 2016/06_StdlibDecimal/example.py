"""Пример использования модуля decimal.

Он реализует тип данных Decimal: десятичные числа с плавающей точкой, которые
представляются точно (а не приблизительно, как float).

Данный тип полезен для финансовых приложений и других применений,
которые требуют точного десятичного представления
"""

import decimal
from decimal import Decimal


# Пример использывания чисел с плавающей запятой
print(1.1 + 2.2)
print()

# Пример использования Decimal
print(Decimal('1.1') + Decimal('2.2'))
print()

# Объекты Decimal неизмяняемы. Параметром конструктора может быть объект типа
# int, str, tuple, float или Decimal. Если value кортеж, то первый аргумент -
# знак, второй - последовательность цифр, третий - позиция запятой.

print(Decimal((0, (1, 4, 1, 4), -4)))


# Операции с Decimal:
decimal.getcontext().prec = 28  # задание точности
print(Decimal(1) / Decimal(7))
print(Decimal('1.2323') * Decimal('3.002323'))
print(Decimal('23320.232') - Decimal('3434.34433'))
print(Decimal(2) ** Decimal('0.5'))
print()

print((-7) % 4)  # 1
print(Decimal(-7) % Decimal(4))  # -3

print(-7 // 4)  # -2
print(Decimal(-7) // Decimal(4))  # -1
