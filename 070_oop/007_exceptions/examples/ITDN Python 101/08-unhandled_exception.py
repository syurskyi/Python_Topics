try:
    raise ValueError
except ZeroDivisionError:
    print('Division by zero')
