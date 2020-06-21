a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError:
    raise ValueError
