# OLD=VERSION===OLD=VERSION===OLD=VERSION
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:  # This else is unnecessary
        return False

# OLD=VERSION===OLD=VERSION===OLD=VERSION


def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False  # We can just return without the else


print(is_odd_number(4))
print(is_odd_number(9))
