def countdown1():
    """Write a generator that counts from 100 to 1"""
    for i in reversed(range(1,101)):
        yield i


def countdown():
    """Write a generator that counts from 100 to 1"""
    num = 100
    while True:
        if num >= 1:
            yield num
            num -= 1
        else:
            break


cd = countdown()
for i in range(101):
    print(next(cd))