___ countdown1():
    """Write a generator that counts from 100 to 1"""
    ___ i __ reversed(r..(1,101)):
        yield i


___ countdown():
    """Write a generator that counts from 100 to 1"""
    num = 100
    while True:
        __ num >= 1:
            yield num
            num -= 1
        ____:
            break


cd = countdown()
___ i __ r..(101):
    print(next(cd))