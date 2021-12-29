def divide_numbers(*, numerator, demoninator ):
    try:
        return int(numerator)/int(demoninator)
    except ZeroDivisionError:
        return 0

print(divide_numbers(3, 5))