import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
rate = 1.45
seconds = 3*60 + 42
cost = rate * seconds / 60
print(cost)


# Example 2
print(round(cost, 2))


# Example 3
rate = 0.05
seconds = 5
cost = rate * seconds / 60
print(cost)


# Example 4
print(round(cost, 2))


# Example 5
from decimal import Decimal
from decimal import ROUND_UP
rate = Decimal('1.45')
seconds = Decimal('222')  # 3*60 + 42
cost = rate * seconds / Decimal('60')
print(cost)


# Example 6
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)


# Example 7
rate = Decimal('0.05')
seconds = Decimal('5')
cost = rate * seconds / Decimal('60')
print(cost)


# Example 8
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)
