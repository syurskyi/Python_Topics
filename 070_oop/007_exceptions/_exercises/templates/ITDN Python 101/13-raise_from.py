a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as error:
    raise ValueError('variable b is incorrect') from error
